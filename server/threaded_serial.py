"""All serial handling with the nordic dongle."""

import asyncio
import functools
import logging
import time
from concurrent.futures import ThreadPoolExecutor

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
        self._read_try_count = 20
        self._read_delay = 0.1
        self.tries = 0
        self.executor = None
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
            self.s = Serial(self.port, baudrate=self.serial_speed)
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

    def _write(self, data):
        _val = b""
        try:
            LOGGER.debug("outgoing: %s", data)
            self.s.write(data)
        except (SerialException, AttributeError) as err:
            LOGGER.error("Problem writing to serial. %s", err)

        _val = self.s.read(1)
        # LOGGER.debug(_val)
        time.sleep(0.5)

        _val += self.s.read(self.s.in_waiting)
        LOGGER.debug("incoming: %s", _val)
        if _val == b"":
            pass
        return _val

    @asyncio.coroutine
    def write(self, data):
        # if self.executor is None:
        #    self.executor = ThreadPoolExecutor(max_workers=1)

        yield from self.messengers.send_outgoing_data(data)

        with ThreadPoolExecutor(max_workers=1) as executor:
            _value = yield from self.loop.run_in_executor(
                executor, (functools.partial(self._write, data))
            )

        # _value = yield from self.loop.run_in_executor(self.executor, functools.partial(self._write,data))

        yield from self.messengers.send_incoming_data(_value)

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
                try:
                    self.s.write(self.id_change)
                except TypeError as err:
                    LOGGER.error(err)
            else:
                yield from self.write(upstring)

        return web.Response(body=b"okay")
