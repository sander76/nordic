import asyncio
import concurrent
import time

from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException

from server.constants import TRYDELAY, NORDIC_CONNECTED, NORDIC_NOT_CONNECTED, SLEEP_BETWEEN_COMMANDS
# from new_server import send_socket_message
from server.helpers import from_string, up_string
from server.nordic import COMMANDS
from server.websocket import send_socket_message

import logging
lgr = logging.getLogger(__name__)


class NordicSerial:
    def __init__(self,loop, serial_port, serial_speed, try_delay=TRYDELAY):
        self.s = Serial()
        self.serial_port = serial_port
        self.s.port = serial_port
        self.s.baudrate = serial_speed
        self.trydelay = try_delay
        self.loop = loop
        # task = asyncio.Task(get_and_print())
        asyncio.Task(self.get_from_serial_port())
        asyncio.Task(self.connect())

    # handler
    def connect(self):
        lgr.info("Connecting to serial port: {}".format(self.serial_port))
        attempt = 1
        while True:
            if self.s.is_open:
                lgr.debug("****************** Connected **************************")
                send_socket_message(NORDIC_CONNECTED)
            else:
                try:
                    lgr.info("Connecting to serial port. Attempt: {}".format(attempt))
                    self.s.open()
                    lgr.info("****************** Connected **************************")
                    send_socket_message(NORDIC_CONNECTED)
                except SerialException:
                    lgr.error("serial port opening problem.")
                    attempt += 1
                    send_socket_message(NORDIC_NOT_CONNECTED)
            yield from asyncio.sleep(self.trydelay)

    # the method which gets wrapped in the asyncio thread executor.
    def get_byte(self):
        while 1:
            if self.s.is_open:
                data = self.s.read(1)
                time.sleep(0.3)
                tst = self.s.read(self.s.inWaiting())
                data += tst
                #data += bytearray(self.s.read(self.s.inWaiting()))
                return data
            time.sleep(self.trydelay)

    # Runs blocking function in executor, yielding the result
    @asyncio.coroutine
    def get_byte_async(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            res = yield from self.loop.run_in_executor(executor, self.get_byte)
            return res

    def get_from_serial_port(self):
        while 1:
            b = yield from self.get_byte_async()
            lgr.debug("incoming: {}".format(b))
            _from = from_string(None,b)
            send_socket_message(_from)

    # handlers.
    def send_nordic(self,request):
        rq = yield from request.json()
        commands = rq['commands']
        first = True
        for cmd in commands['commands']:
            upstring = COMMANDS.get(cmd)
            if upstring is not None:
                if first:
                    first = False
                else:
                    # get the delay value or use default SLEEP_BETWEEN_COMMANDS
                    delay = commands.get("delay", SLEEP_BETWEEN_COMMANDS)
                    yield from asyncio.sleep(delay)
                try:
                    self.s.write(upstring)
                    _up = up_string(cmd,upstring)
                    lgr.debug(_up)
                    send_socket_message(_up)
                except SerialException:
                    lgr.exception("writing to serial port failure.")
                    self.s.close()
                    send_socket_message(NORDIC_NOT_CONNECTED)
                    # return web.Response(text="Writing to blind went wrong. Please check cables and USB dongle")
            else:
                lgr.error("sending command {} did not succeed.".format(cmd))
                return web.Response(text="sending command {} did not succeed.".format(cmd), status=500)
        return web.Response(body=b"okay")
