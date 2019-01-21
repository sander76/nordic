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
    connecting = 3
    connected = 4


class NordicSerial:
    def __init__(self, loop, serial_port, serial_speed, messengers=None):
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
        self.state = State.disconnected
        self.connector = self.loop.create_task(self.connector())

    def disconnect(self):
        LOGGER.debug("Disconnecting from serial")
        self.state = State.disconnected
        if self.s is not None:
            try:
                self.s.close()
            except Exception as err:
                LOGGER.error(err)
        self.s = None

    @asyncio.coroutine
    def connector(self):
        try:
            """Check connection state in a loop"""
            while True:
                LOGGER.debug("Checking connection.")
                if self.state == State.disconnected:
                    LOGGER.debug("Connecting.")
                    yield from self.connect()

                yield from asyncio.sleep(5)
        except Exception as err:
            LOGGER.error(err)

    def change_dongle_id(self):
        if self.state in (State.connected, State.connecting):
            self.s.write(self.id_change)

    @asyncio.coroutine
    def connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""
        self.state = State.connecting
        yield from self.send_connection_status()

        LOGGER.debug(
            "Connecting to serial port %s. Attempt: %s",
            self.serial_speed,
            self.tries,
        )
        try:
            self.s = Serial(self.port, baudrate=self.serial_speed, timeout=1)
        except SerialException:
            self.state = State.disconnected
            yield from self.send_connection_status()
            LOGGER.error("Problem connecting")
            return

        yield from asyncio.sleep(1)
        LOGGER.info("Changing dongle id.")
        self.s.write(self.id_change)

        self.state = State.connected
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

    def _read(self, data):
        try:
            # this method takes place in a separate thread.
            _val = b""

            _val = self.s.read(1)
            if _val == b"":
                LOGGER.warning("No response recieved from serial.")
                return _val

            time.sleep(0.3)
            _val += self.s.read(self.s.in_waiting)

            LOGGER.debug("incoming: %s", _val)

            return _val
        except Exception as err:
            LOGGER.error(err)

    @asyncio.coroutine
    def write(self, data):
        try:
            LOGGER.debug("outgoing %s", data)
            self.s.write(data)
            yield from self.messengers.send_outgoing_data(data)
        except (SerialException, AttributeError, Exception) as err:
            LOGGER.error("Problem writing to serial. %s", err)
            self.disconnect()
            raise NordicWriteProblem(
                "Problem writing to serial. {}".format(err)
            )
        else:

            with ThreadPoolExecutor(max_workers=1) as executor:
                _value = yield from self.loop.run_in_executor(
                    executor, (functools.partial(self._read, data))
                )

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
                    self.change_dongle_id()
                except TypeError as err:
                    LOGGER.error(err)
            else:
                try:
                    yield from self.write(upstring)
                except NordicWriteProblem as err:
                    LOGGER.error(err)

                    # todo: return a proper error response.
                    return

        return web.Response(body=b"okay")
