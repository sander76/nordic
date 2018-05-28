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


class NordicSerial:
    def __init__(self, loop, serial_port, serial_speed,
                 try_delay=TRYDELAY, messengers=None):
        self._network_id = get_id()
        self.network_id = byte_to_string_rep(
            self._network_id)
        self.id_change = b'\x00\x03I' + self._network_id
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
        self.need_reset = False

        self._read_try_count = 10
        self._read_loop = 0.2
        self._waiting_for_input = False

    @property
    def serial_connected(self):
        if self.s is None or not self.s.is_open:
            return False
        else:
            return True

    def get_connection_status(self):
        return {"nordic": self.serial_connected, "networkid": self.network_id}

    @asyncio.coroutine
    def send_connection_status(self):
        LOGGER.debug("Sending message status.")
        yield from self.messengers.send_message(
            self.get_connection_status()
        )

    @asyncio.coroutine
    def connect(self):
        """Continuously trying to connect to the serial port in a loop."""
        while True:
            if self.serial_connected:
                yield from self._watch()
            if self.need_reset:
                LOGGER.info("Resetting serial.")
                self._waiting_for_input = False

                if self.s:

                    self.s.reset_input_buffer()
                    self.s.reset_output_buffer()
                    try:
                        self.s.close()
                    except (Exception) as err:
                        LOGGER.exception(err)
                self.s = None
                self.need_reset = False
                yield from asyncio.sleep(1)
            if not self.serial_connected:
                yield from self._connect()
            yield from asyncio.sleep(min(self.connect_attempts, 10))

    @asyncio.coroutine
    def _connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""
        try:
            LOGGER.debug("Connecting to serial port %s. Attempt: %s",
                         self.serial_speed, self.connect_attempts)
            self.s = Serial(self.port, baudrate=self.serial_speed, timeout=0)
            yield from self.send_queue.put(self.id_change)
            yield from self.send_connection_status()
            self.connect_attempts = 1
            LOGGER.info("Connected to serial port {}".format(self.s.port))
        except (SerialException, FileNotFoundError, Exception) as err:
            self.need_reset = True
            LOGGER.error('Problem connecting. %s', err)
            self.connect_attempts += 1
            yield from self.send_connection_status()

    @asyncio.coroutine
    def _watch(self):
        try:
            if not self._waiting_for_input:
                _val = self.s.read()
        except Exception as err:
            LOGGER.error("Watchdog failed: %s", err)
            self.need_reset = True

    @asyncio.coroutine
    def _write(self, data):
        _val = None
        tries = self._read_try_count
        self.s.write(data)
        self._waiting_for_input = True
        yield from self.messengers.send_outgoing_data(data)
        yield from asyncio.sleep(0.3)
        while tries > 0:

            _val = self.s.read()
            if _val:
                yield from asyncio.sleep(self._read_loop)
                _val += self.s.read(self.s.in_waiting)
                break
            yield from asyncio.sleep(self._read_loop)
            tries -= 1
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
            if self.serial_connected and not self.need_reset:
                try:
                    _val = yield from self._write(upstring)
                    if _val:
                        LOGGER.debug("incoming %s", _val)
                        yield from self.messengers.send_incoming_data(_val)
                    else:
                        LOGGER.error("No response received. Resetting.")
                        self.need_reset = True
                except Exception as err:
                    LOGGER.exception(err)
                    self.need_reset = True

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
