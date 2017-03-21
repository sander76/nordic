"""
All serial handling with the nordic dongle.

"""

import asyncio
import time
from threading import Thread

from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException
from server.constants import TRYDELAY, SLEEP_BETWEEN_COMMANDS
from server.nordic import Nd


import logging

lgr = logging.getLogger(__name__)


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
    def __init__(self, loop, serial_port, serial_speed, network_id,
                 try_delay=TRYDELAY, messengers=None):
        self.network_id = byte_to_string_rep(
            network_id)  # string representation of the network id. in hex.
        self.id_change = b'\x00\x03I' + network_id
        self.s = Serial()
        self.s.port = serial_port
        self.s.baudrate = serial_speed
        self.trydelay = try_delay  # Delay time between connection tries
        self.loop = loop  # The main event loop.
        self.loop.create_task(self.connect())
        self.loop.create_task(self._write_to_nordic())
        self.messengers = messengers
        self.incoming = False
        self.connect_attempts = 1
        self.send_queue = asyncio.Queue(loop=loop)
        self.refresh_count = 1
        self.t = Thread(target=self.get_byte)
        self.t.start()

    @asyncio.coroutine
    def send_connection_status(self, connected, network_id):
        yield from self.messengers.send_message(
            {"nordic": connected, "networkid": network_id})

    @asyncio.coroutine
    def connect(self):
        """Continuously trying to connect to the serial port in a loop."""
        while True:
            if self.s.is_open:
                if self.refresh_count > 10:
                    yield from self.send_connection_status(True,
                                                           self.network_id)
                    self.refresh_count = 1
                else:
                    self.refresh_count += 1
            else:
                yield from self._connect()
            yield from asyncio.sleep(self.trydelay)

    @asyncio.coroutine
    def _connect(self):
        """Connects to the serial port and prepares the nordic
        for sending commands to the blinds."""
        try:
            lgr.info("Connecting to serial port {}. Attempt: {}".format(
                self.s.port, self.connect_attempts))
            self.s.open()
            # The nordic chip has been reset.
            yield from self.send_queue.put(self.id_change)
            yield from self.send_connection_status(True, self.network_id)
        except SerialException:
            lgr.error("serial port opening problem.")
            self.connect_attempts += 1
            yield from self.send_connection_status(False, "unknown")

    def get_byte(self):
        """Method to be run inside a separate thread continuously checking
        incoming data. When incoming data is captured it is sent
        back to the main event loop."""
        while 1:
            try:
                data = self.s.read(1)
                time.sleep(0.5)
                tst = self.s.read(self.s.inWaiting())
                data += tst
                # run coroutine in main loop with the captured serial data.
                self.loop.call_soon_threadsafe(self.set_incoming_serial,data,)
                # asyncio.run_coroutine_threadsafe(
                #     self.set_incoming_serial(data), self.loop)
            except SerialException:
                lgr.error("error reading from serial port")
                time.sleep(1)

    # @asyncio.coroutine
    # def set_incoming_serial(self, data):
    #     """Method to be called from the serial thread capturing input.
    #     This method notifies the main loop that data has come in from
    #     the serial port."""
    #     self.incoming = True
    #     yield from self.messengers.send_incoming_data(data)

    def set_incoming_serial(self,data):
        self.incoming=True
        self.loop.create_task(self.messengers.send_incoming_data(data))

    @asyncio.coroutine
    def reset_serial(self):
        self.s.close()
        yield from self.send_connection_status(False, None)

    @asyncio.coroutine
    def _write_to_nordic(self):
        """ Coroutine which is added to the main event loop.
        It checks a queue for data to be sent to the nordic chip.
        Also starts an incoming check to see whether a response is coming in.
        If not the nordic connection will be reset."""
        while 1:
            # check the message queue for messages.
            upstring = yield from self.send_queue.get()
            # lgr.debug("queue size: {}".format(self.send_queue.qsize()))
            # self.send_queue.task_done()
            self.incoming = False
            sent = False
            while not sent:
                try:
                    self.s.write(upstring)
                    sent = True
                except SerialException:
                    lgr.debug("serial port not open. Retrying...")
                    yield from asyncio.sleep(1)
            yield from self.messengers.send_outgoing_data(upstring)
            yield from self._incoming_check()


    @asyncio.coroutine
    def _incoming_check(self):
        tries = 0
        while tries < 6:
            if self.incoming:
                self.incoming = False
                return
            yield from asyncio.sleep(0.5)
            tries += 1
        # No incoming data detected. Resetting connection.
        yield from self.reset_serial()

    @asyncio.coroutine
    def send_nordic(self, request):
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
