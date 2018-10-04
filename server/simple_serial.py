"""All serial handling with the nordic dongle."""

import asyncio
import logging
import time

from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException

from server.constants import TRYDELAY, SLEEP_BETWEEN_COMMANDS
from server.id_generator import get_id
from server.nordic import Nd

LOGGER = logging.getLogger(__name__)


class NordicConnectionProblem(Exception):
    pass


class NordicWriteProblem(NordicConnectionProblem):
    pass


class NordicReadProblem(NordicConnectionProblem):
    pass


def byte_to_string_rep(byte_instance):
    string_rep = []
    for bt in byte_instance:
        if 32 <= bt < 127:
            string_rep.append(chr(bt))
        else:
            string_rep.append(hex(bt))
    _string_rep = "".join(string_rep)
    return _string_rep


from enum import Enum


class State(Enum):
    connected = 1
    need_reset = 2
    connecting = 3
    disconnected = 4
    waiting_for_input = 5
    watching = 6


class NordicSerial:
    def __init__(
        self,
        loop,
        serial_port,
        serial_speed,
        try_delay=TRYDELAY,
        messengers=None,
    ):
        self._network_id = get_id()
        self.network_id = byte_to_string_rep(self._network_id)
        self.id_change = b"\x00\x03i" + self._network_id
        self.id_change_response = b"\x03i" + self._network_id
        self.s = None
        self.messengers = messengers
        self.port = serial_port
        self.serial_speed = serial_speed
        self.connect_attempts = 1
        self.loop = loop  # The main event loop.
        self.loop.create_task(self.connector())
        self._read_try_count = 10
        self._read_delay = 0.1

        self.state = State.disconnected


    def disconnect(self):
        # todo: Close port first.
        if self.s is not None:
            try:
                self.s.close()
            except Exception as err:
                LOGGER.error(err)

    @asyncio.coroutine
    def connector(self):
        while True:
            LOGGER.info("Checking connection")
            if self.s is None or self.s.closed:
                yield from self.connect()
            yield from asyncio.sleep(5)

    @asyncio.coroutine
    def connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""

        yield from self.send_connection_status()

        try:
            LOGGER.debug(
                "Connecting to serial port %s. Attempt: %s",
                self.serial_speed,
                self.connect_attempts,
            )
            self.s = Serial(self.port, baudrate=self.serial_speed, timeout=0)

            yield from asyncio.sleep(1)
            LOGGER.info("Changing dongle id.")
            self.s.write(self.id_change)

            # Connecting succeeded.
            self.connect_attempts = 1
            self.state = State.connected
            LOGGER.info("Connected to serial port {}".format(self.s.port))
        except (SerialException, FileNotFoundError, Exception) as err:
            self.state = State.need_reset
            LOGGER.error("Problem connecting. %s", err)
            self.connect_attempts += 1
        finally:
            yield from self.send_connection_status()

    def get_connection_status(self):
        if self.s is None or self.s.closed:
            _connected = False
        else:
            _connected = True
        return {"nordic": _connected, "networkid": self.network_id}

    @asyncio.coroutine
    def send_connection_status(self):
        LOGGER.debug("Sending message status.")
        yield from self.messengers.send_message(self.get_connection_status())

    @asyncio.coroutine
    def _write(self, data):

        _val = None
        try:
            LOGGER.debug("outgoing: %s", data)
            self.s.write(data)
        except (SerialException,AttributeError) as err:
            LOGGER.error("Problem writing to serial. %s", err)
            raise NordicWriteProblem()
        yield from self.messengers.send_outgoing_data(data)

        for i in range(self._read_try_count):
            _val = self.s.read()
            if _val:
                yield from asyncio.sleep(self._read_delay)
                _val += self.s.read(self.s.in_waiting)
                break
            yield from asyncio.sleep(self._read_delay)
        if _val is None:
            LOGGER.error("Problem reading from serial")
            raise NordicReadProblem()

        yield from self.messengers.send_incoming_data(_val)

    @asyncio.coroutine
    def write(self, data):
        tries = 0

        try:
            yield from self._write(data)
        except NordicConnectionProblem:
            LOGGER.info("Connection try %s", tries)
            if tries > 2:
                yield from asyncio.sleep(tries * 1)
                self.disconnect()
                yield from self.connect()
                yield from self._write(data)
            else:
                yield from self.messengers.send
            tries += 1

    @asyncio.coroutine
    def send_nordic(self, request):
        # LOGGER.debug("Request received from User interface")
        rq = yield from request.json()
        commands = rq["commands"]
        # incoming is a list of commands. First command has simpler structure
        # and parsing is simpler so this bool keeps track whether to do the
        # first parsing or the other parsing.
        first = True
        for cmd in commands:
            if first:
                upstring = Nd[cmd].value
                first = False
            else:
                upstring = Nd[cmd["command"]].value
                delay = cmd.get("delay", SLEEP_BETWEEN_COMMANDS)
                yield from asyncio.sleep(delay)
            try:
                yield from self._write(upstring)
            except NordicConnectionProblem:
                # todo: loop and throttle this.
                yield from self.connect()
                yield from self.write(upstring)

        return web.Response(body=b"okay")
