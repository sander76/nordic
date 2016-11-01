import asyncio
import concurrent
import time

from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException, portNotOpenError
from server.constants import TRYDELAY, SLEEP_BETWEEN_COMMANDS
from server.helpers import from_string, up_string
from server.messenger import Messengers
from server.nordic import COMMANDS

import logging

lgr = logging.getLogger(__name__)


def byte_to_string_rep(byte_instance):
    string_rep = []
    for bt in byte_instance:
        if bt >= 32 and bt < 127:
            string_rep.append(chr(bt))
        else:
            string_rep.append(hex(bt))
    _string_rep = ''.join(string_rep)
    return _string_rep


class NordicSerial:
    def __init__(self, loop, serial_port, serial_speed, network_id, try_delay=TRYDELAY, messengers=Messengers()):
        # self.network_id = b'\x00\x03I' + network_id
        self.network_id = byte_to_string_rep(network_id)  # string representation of the network id. in hex.
        self.id_change = b'\x00\x03I' + network_id  # the bytes object to send to nordic to change the network id of the dongle.
        self.s = Serial()
        self.serial_port = serial_port
        self.s.port = serial_port
        self.s.baudrate = serial_speed
        self.trydelay = try_delay
        self.loop = loop
        self.loop.create_task(self.connect())
        self.messengers = messengers
        self.incoming = False

    def send_connection_status(self, connected, network_id):
        self.messengers.send_message({"nordic": connected, "networkid": network_id})

    # handler
    @asyncio.coroutine
    def connect(self):
        # lgr.info("Connecting to serial port: {}".format(self.serial_port))
        attempt = 1
        while True:
            if self.s.is_open:
                lgr.debug("****************** Already Connected **************************")
                self.send_connection_status(True, self.network_id)
            else:
                try:
                    lgr.info("Connecting to serial port {}. Attempt: {}".format(self.serial_port, attempt))
                    self.s.open()
                    # serial port is open. Adding a incoming listener is okay now.

                    # check all tasks:
                    # tasks = asyncio.Task.all_tasks(self.loop)
                    self.loop.create_task(self.get_from_serial_port())
                    # yield from asyncio.sleep()
                    yield from self._write_to_nordic(self.id_change)
                    self.send_connection_status(True, self.network_id)
                except SerialException:
                    lgr.error("serial port opening problem.")
                    attempt += 1
                    self.send_connection_status(False, "unknown")
            yield from asyncio.sleep(self.trydelay)

    # the method which gets wrapped in the asyncio thread executor.
    def get_byte(self):
        # while 1:
        # if self.s.is_open:
        data = self.s.read(1)
        time.sleep(0.5)
        tst = self.s.read(self.s.inWaiting())
        data += tst
        return data
        # except SerialException as e:
        #     lgr.exception(e)
        #   time.sleep(self.trydelay)

    # Runs blocking function in executor, yielding the result
    @asyncio.coroutine
    def get_byte_async(self):
        # try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            res = yield from self.loop.run_in_executor(executor, self.get_byte)
            return res
        #        except SerialException as e:
        #            self.s.close()

    @asyncio.coroutine
    def get_from_serial_port(self):
        while 1:
            try:
                b = yield from self.get_byte_async()
                lgr.debug("incoming: {}".format(b))
                self.incoming = True
                _from = from_string(None, b)
                self.messengers.send_message(_from)
            except SerialException as e:
                self.close_serial()
                break

    def close_serial(self):
        self.s.close()
        self.send_connection_status(False, None)

    @asyncio.coroutine
    def _write_to_nordic(self, upstring):
        self.s.write(upstring)
        _up = up_string(None, upstring)
        lgr.debug(_up)
        self.messengers.send_message(_up)
        yield from self._incoming_check()

    @asyncio.coroutine
    def _incoming_check(self):
        tries = 0
        while tries < 4:
            if self.incoming:
                self.incoming = False
                return
            yield from asyncio.sleep(1)
            tries += 1
        # incoming should be true after something has been sent.
        # resetting connection:
        self.close_serial()

    @asyncio.coroutine
    def send_nordic(self, request):
        rq = yield from request.json()
        commands = rq['commands']
        first = True
        for cmd in commands:
            if first:
                upstring = COMMANDS.get(cmd)
                first = False
            else:
                upstring = COMMANDS.get(cmd['command'])
                # get the delay value or use default SLEEP_BETWEEN_COMMANDS
                delay = cmd.get('delay', SLEEP_BETWEEN_COMMANDS)
                yield from asyncio.sleep(delay)
            try:
                yield from self._write_to_nordic(upstring)
            except SerialException:
                lgr.exception("writing to serial port failure.")
                self.close_serial()
        return web.Response(body=b"okay")
