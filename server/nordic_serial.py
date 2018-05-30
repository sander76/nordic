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


def byte_to_string_rep(byte_instance):
    string_rep = []
    for bt in byte_instance:
        if 32 <= bt < 127:
            string_rep.append(chr(bt))
        else:
            string_rep.append(hex(bt))
    _string_rep = ''.join(string_rep)
    return _string_rep


from enum import Enum


class State(Enum):
    connected = 1
    need_reset = 2
    connecting = 3
    disconnected = 4


class NordicSerial:
    def __init__(self, loop, serial_port, serial_speed,
                 try_delay=TRYDELAY, messengers=None):
        self._network_id = get_id()
        self.network_id = byte_to_string_rep(
            self._network_id)
        self.id_change = b'\x00\x03I' + self._network_id
        self.id_change_response = b'\x03I' + self._network_id
        self.s = None

        self.port = serial_port
        self.serial_speed = serial_speed
        self.trydelay = try_delay  # Delay time between connection tries
        self.connect_attempts = 1
        self.loop = loop  # The main event loop.
        self.loop.create_task(self.connect())
        self.loop.create_task(self._write_to_nordic())
        self.messengers = messengers
        self.send_queue = asyncio.Queue(loop=loop)

        self._read_try_count = 10
        self._read_loop = 0.2
        self._waiting_for_input = False

        self.state = State.disconnected

    def get_connection_status(self):
        if self.state == State.connected:
            _connected = True
        else:
            _connected = False
        return {"nordic": _connected, "networkid": self.network_id}

    @asyncio.coroutine
    def send_connection_status(self):
        LOGGER.debug("Sending message status.")
        yield from self.messengers.send_message(
            self.get_connection_status()
        )

    @asyncio.coroutine
    def connect(self):
        """Continuously trying to connect to the serial port in a loop."""
        LOGGER.info("Starting connection loop.")

        while True:
            if self.state == State.connected:
                yield from self._watch()
            if self.state == State.need_reset:
                yield from self._reset()
            if self.state == State.disconnected:
                yield from self._connect()

            yield from asyncio.sleep(1)

    @asyncio.coroutine
    def _reset(self):
        yield from self.send_connection_status()
        LOGGER.info("Resetting serial.")
        self._waiting_for_input = False

        if self.s:
            try:
                self.s.close()
            except (Exception) as err:
                LOGGER.error("Closing error: %s", err)
        self.state = State.disconnected
        yield from asyncio.sleep(2)

    @asyncio.coroutine
    def _connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""
        try:

            LOGGER.debug("Connecting to serial port %s. Attempt: %s",
                         self.serial_speed, self.connect_attempts)
            if self.s is None:
                self.s = Serial(self.port, baudrate=self.serial_speed,
                                timeout=0)
            else:
                self.s.open()

            yield from asyncio.sleep(1)

            _val = yield from self._write(self.id_change)
            LOGGER.debug("Incoming on connect: %s", _val)

            if _val and self.id_change_response in _val:
                yield from self.messengers.send_incoming_data(_val)
            else:
                self.state = State.need_reset
                return

            # Connecting succeeded.
            self.connect_attempts = 1
            self.state = State.connected
            LOGGER.info("Connected to serial port {}".format(self.s.port))
        except (SerialException, FileNotFoundError, Exception) as err:
            self.state = State.need_reset
            LOGGER.error('Problem connecting. %s', err)
            self.connect_attempts += 1
        finally:
            yield from self.send_connection_status()

    @asyncio.coroutine
    def _watch(self):
        try:
            if not self._waiting_for_input:
                self.s.read()
        except Exception as err:
            LOGGER.error("Watchdog failed: %s", err)
            self.state = State.need_reset

    @asyncio.coroutine
    def _write(self, data):
        _val = None
        tries = self._read_try_count
        self._waiting_for_input = True
        #self.s.close()
        #yield from asyncio.sleep(1)
        #self.s.open()
        #yield from asyncio.sleep(0.5)
        # self.s.close()
        # yield from asyncio.sleep(1)
        # self.s.open()
        try:
            self.s.write(data)
        except Exception as err:
            LOGGER.error("Problem writing to serial. %s", err)
            self.state = State.need_reset
            return False
        yield from self.messengers.send_outgoing_data(data)

        yield from asyncio.sleep(0.1)
        while tries > 0:
            _val = self.s.read()
            if _val:
                yield from asyncio.sleep(self._read_loop)
                _val += self.s.read(self.s.in_waiting)
                break
            yield from asyncio.sleep(self._read_loop)
            tries -= 1
        yield from asyncio.sleep(0.4)
        self._waiting_for_input = False
        return _val

    @asyncio.coroutine
    def _write_to_nordic(self):
        """ Coroutine which is added to the main event loop.
        It checks a queue for data to be sent to the nordic chip.
        Also starts an incoming check to see whether a response is coming in.
        If not the nordic connection will be reset."""
        while True:
            # check the message queue for messages.
            LOGGER.debug("waiting for incoming user commands")
            upstring = yield from self.send_queue.get()
            if self.state == State.connected:
                try:
                    _val = yield from self._write(upstring)
                    if _val:
                        LOGGER.debug("incoming %s", _val)
                        yield from self.messengers.send_incoming_data(_val)
                    else:
                        LOGGER.error("No response received. Resetting.")
                        self.state = State.need_reset
                        # self.need_reset = True
                except Exception as err:
                    LOGGER.exception(err)
                    self.state = State.need_reset
                    # self.need_reset = True

    @asyncio.coroutine
    def send_nordic(self, request):
        LOGGER.debug("Request received from User interface")
        rq = yield from request.json()
        commands = rq['commands']
        # incoming is a list of commands. First command has simpler structure
        # and parsing is simpler so this bool keeps track whether to do the
        # first parsing or the other parsing.
        first = True
        for cmd in commands:
            if first:
                upstring = Nd[cmd].value
                first = False
            else:
                upstring = Nd[cmd['command']].value
                # get the delay value or use default SLEEP_BETWEEN_COMMANDS
                delay = cmd.get('delay', SLEEP_BETWEEN_COMMANDS)
                yield from asyncio.sleep(delay)
            yield from self.send_queue.put(upstring)
        return web.Response(body=b"okay")
