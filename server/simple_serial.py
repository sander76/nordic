"""All serial handling with the nordic dongle."""

import asyncio
import logging

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
    disconnected = 0
    idle = 1
    writing = 2


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
        LOGGER.info("network id: {}".format(self._network_id))
        self.network_id = byte_to_string_rep(self._network_id)
        self.id_change = b"\x00\x03i" + self._network_id
        self.id_change_response = b"\x03i" + self._network_id
        self.s = None
        self.messengers = messengers
        self.port = serial_port
        self.serial_speed = serial_speed
        self.loop = loop
        self.loop.create_task(self.connector())
        self._read_try_count = 10
        self._read_delay = 0.1
        self.tries = 0

        self.state = State.idle

    def disconnect(self):
        LOGGER.debug("Disconnecting from serial")
        if self.s is not None:
            try:
                self.s.close()
            except Exception as err:
                LOGGER.error(err)
        self.s = None

    @asyncio.coroutine
    def connector(self):
        """Check connection state in a loop"""
        while True:
            if self.state == State.idle:
                LOGGER.debug("Checking connection")
                if self.s is not None:
                    LOGGER.debug(self.s.closed)
                if self.s is None or self.s.closed:
                    LOGGER.info("Trying to connect")
                    yield from self.connect()

            yield from asyncio.sleep(5)

    @asyncio.coroutine
    def connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""

        yield from self.send_connection_status()

        LOGGER.debug(
            "Connecting to serial port %s. Attempt: %s",
            self.serial_speed,
            self.tries,
        )
        try:
            self.s = Serial(self.port, baudrate=self.serial_speed, timeout=0)
        except SerialException:
            yield from self.send_connection_status()
            LOGGER.error("Problem connecting")
            return

        yield from asyncio.sleep(1)
        LOGGER.info("Changing dongle id.")
        self.s.write(self.id_change)

        LOGGER.info("Connected to serial port %s", self.s.port)

        yield from self.send_connection_status()

    def get_connection_status(self):

        if self.s is None or self.s.closed:
            _connected = False
        else:
            _connected = True
        return {"nordic": _connected, "networkid": self.network_id}

    @asyncio.coroutine
    def send_connection_status(self):
        status = self.get_connection_status()
        LOGGER.debug("Sending connection status. %s", status)
        yield from self.messengers.send_message(status)

    @asyncio.coroutine
    def _write(self, data):
        _val = None
        try:
            LOGGER.debug("outgoing: %s", data)
            self.s.write(data)
        except (SerialException, AttributeError) as err:
            LOGGER.error("Problem writing to serial. %s", err)

            raise NordicWriteProblem()
        yield from self.messengers.send_outgoing_data(data)

        for i in range(self._read_try_count):
            # LOGGER.info("read try count %s",i)
            _val = self.s.read()
            if _val:
                yield from asyncio.sleep(self._read_delay)
                _val += self.s.read(self.s.in_waiting)
                break
            yield from asyncio.sleep(self._read_delay)
        if _val is None:
            LOGGER.error("Problem reading from serial")
            raise NordicReadProblem()
        LOGGER.debug("response: %s",_val)
        yield from self.messengers.send_incoming_data(_val)

    @asyncio.coroutine
    def write(self, data):
        self.state = State.writing
        try:
            yield from self._write(data)

        except NordicConnectionProblem:
            self.disconnect()

            self.tries += 1
            LOGGER.warning("Write retry %s", self.tries)
            if self.tries < 2:
                yield from asyncio.sleep((self.tries - 1) * 1)
                yield from self.connect()
                yield from self.write(data)
            else:
                LOGGER.error("unable to send command.")
                self.tries = 0
                self.state = State.idle
                yield from self.send_connection_status()
        else:
            self.state = State.idle
            LOGGER.debug("changing state to %s", self.state)
            self.tries = 0

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
            if upstring == Nd.SET_DONGLE_ID.value:
                yield from self.s.write(self.id_change)
            else:
                yield from self.write(upstring)

        return web.Response(body=b"okay")
