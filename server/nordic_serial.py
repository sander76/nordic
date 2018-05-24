"""All serial handling with the nordic dongle."""

import asyncio
import logging
import time
from threading import Thread, Condition

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


class MockSerial:
    def __init__(self):
        self._is_open = True
        self._port = None
        self._return_string = "no_serial"
        self._old_char_count = 0
        self.cv = Condition()
        self._incoming = False

    @property
    def is_open(self):
        return self._is_open

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    def open(self):
        self._is_open = True

    def read(self, chars):
        if chars is None:
            return b''
        self.cv.acquire()
        while not self._incoming:
            self.cv.wait()
        data = self._incoming
        self._incoming = False
        self.cv.release()
        return data

    def inWaiting(self):
        return None

    def write(self, data):
        self.cv.acquire()
        self._incoming = data
        self.cv.notify()
        self.cv.release()
        LOGGER.debug(data)


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
        self.incoming = False  # Flag is set when data is to be expected.
        self.resetting = True  # Flag is set when serial port is being reset.
        self.connect_attempts = 1
        self.t = Thread(target=self.get_byte)
        self.t.start()
        self.loop = loop  # The main event loop.
        self.loop.create_task(self.connect())
        self.loop.create_task(self._write_to_nordic())
        self.messengers = messengers
        self.send_queue = asyncio.Queue(loop=loop)

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
            if not self.serial_connected:
                yield from self._connect()
            yield from asyncio.sleep(self.trydelay)

    @asyncio.coroutine
    def _connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""
        try:
            LOGGER.info("Connecting to serial port {}. Attempt: {}".format(
                self.serial_speed, self.connect_attempts))
            self.s = Serial(self.port, baudrate=self.serial_speed)
            yield from self.send_queue.put(self.id_change)
            yield from self.send_connection_status()
            self.resetting = False
            LOGGER.info("Connected to serial port {}".format(self.s.port))
        except SerialException as err:

            LOGGER.error(err)
            self.connect_attempts += 1
            yield from self.send_connection_status()

    def get_byte(self):
        """Method to be run inside a separate thread continuously checking
        incoming data. When incoming data is captured it is sent
        back to the main event loop."""
        LOGGER.info("start looking for incoming data.")
        while True:
            if self.serial_connected:
                try:
                    data = self.s.read(1)
                    time.sleep(0.1)
                    tst = self.s.read(self.s.inWaiting())
                    data += tst
                    # run coroutine in main loop with the captured serial data.
                    self.loop.call_soon_threadsafe(self.set_incoming_serial,
                                                   data)
                except SerialException as err:

                    LOGGER.info("error reading from serial port. Resetting it")
                    LOGGER.error(err)

                    # if not self.resetting:
                    #     self.resetting = True

                    self.loop.call_soon_threadsafe(self.threaded_reset_serial)
                    # while self.resetting:
                    #     time.sleep(1)
                except Exception as err:
                    LOGGER.error(err)
            else:
                time.sleep(1)

    def threaded_reset_serial(self):
        self.loop.create_task(self.reset_serial())

    def set_incoming_serial(self, data):
        self.incoming = True
        self.loop.create_task(self.messengers.send_incoming_data(data))

    @asyncio.coroutine
    def reset_serial(self):
        if not self.resetting:
            LOGGER.debug("resetting serial")
            self.resetting = True

            LOGGER.debug("closing serial connection")
            try:
                self.s.close()
            except Exception as err:
                LOGGER.error(err)
            self.s = None

            yield from self.send_connection_status()
            # self.s.dtr = False
            # time.sleep(0.05)
            # self.s.dtr = True
            # time.sleep(0.05)
            # yield from self._connect()

    @asyncio.coroutine
    def _write_to_nordic(self):
        """ Coroutine which is added to the main event loop.
        It checks a queue for data to be sent to the nordic chip.
        Also starts an incoming check to see whether a response is coming in.
        If not the nordic connection will be reset."""
        while True:
            try:
                # check the message queue for messages.
                LOGGER.debug("waiting for incoming user commands")
                upstring = yield from self.send_queue.get()
                self.incoming = False
                if self.serial_connected:
                    try:
                        self.s.write(upstring)
                    except SerialException as err:
                        LOGGER.error(err)
                        yield from self.reset_serial()
                    else:
                        yield from self.messengers.send_outgoing_data(
                            upstring)
                        yield from self._incoming_check()
                else:
                    LOGGER.error("Writing failed. Port is closed.")
            except Exception as err:
                LOGGER.exception(err)
                yield from asyncio.sleep(1)

    @asyncio.coroutine
    def _incoming_check(self):
        LOGGER.debug("Checking for dongle response.")
        tries = 0
        while tries < 6:
            if self.incoming:
                LOGGER.debug("Dongle response received.")
                self.incoming = False
                return
            yield from asyncio.sleep(0.5)
            tries += 1
        LOGGER.debug("No dongle response received.")
        yield from self.reset_serial()

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
