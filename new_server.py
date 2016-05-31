import argparse
import asyncio
import concurrent
import time

from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException

from fake_serial import FakeSerial
from helpers import view_factory
from nordic import COMMANDS

# Normal serial blocking reads
# This could also do any processing required on the data
from websocket import websocket_handler
import logging
import logging.handlers

# from async_serial import get_and_print
# SERIAL_PORT = "COM11"
SERIAL_SPEED = 38400
SLEEP_BETWEEN_COMMANDS = 2

lgr = logging.getLogger(__name__)


def get_byte():
    data = bytearray(s.read(1))
    time.sleep(0.3)
    data += bytearray(s.read(s.inWaiting()))
    return data


# Runs blocking function in executor, yielding the result
@asyncio.coroutine
def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        res = yield from loop.run_in_executor(executor, get_byte)
        return res


def get_and_print():
    while 1:
        b = yield from get_byte_async()
        msg = "from nordic: {}".format(repr(b))
        lgr.info(msg)
        send_socket_message(msg)


task = asyncio.Task(get_and_print())


def send_socket_message(message):
    for ws in app['sockets']:
        ws.send_str(message)


def send_nordic(request):
    rq = yield from request.json()
    commands = rq['commands']
    first = True
    for cmd in commands['commands']:
        upstring = COMMANDS.get(cmd)
        if upstring is not None:
            if first:
                first = False
            else:
                delay = commands.get("delay",SLEEP_BETWEEN_COMMANDS)
                yield from asyncio.sleep(delay)
            s.write(upstring)
            #send_socket_message("sending: {}".format(upstring))
            msg = "to nordic: {} {}".format(cmd, upstring)
            send_socket_message(msg)
            lgr.info(msg)
            #
        else:
            lgr.error("sending command {} did not succeed.".format(cmd))
            return web.Response(body=b"not okay", status=500)
    return web.Response(body=b"okay")


parser = argparse.ArgumentParser()
parser.add_argument("--serialport")
args = parser.parse_args()

# setup the serial port.
if args.serialport:
    try:
        SERIAL_PORT = args.serialport
        s = Serial(SERIAL_PORT, SERIAL_SPEED)
    except SerialException as e:
        lgr.exception(e)
else:
    s = FakeSerial()

# create the app instance and get the async loop.
app = web.Application()
loop = app.loop

# create some routes.
app.router.add_route('POST', '/nordic', send_nordic)
app.router.add_route("GET", '/app/', view_factory('/', 'static/app/index.html'))
app.router.add_static("/app/", "static/app/")

# add the websocket address
app.router.add_route('GET', '/ws', websocket_handler)
# keep a list with all websocket connections.
app['sockets'] = []

lgr.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.handlers.RotatingFileHandler("nordic.log", 'a', 1000, 5)
fh.setLevel(logging.ERROR)

lgr.addHandler(ch)
lgr.addHandler(fh)
try:
    web.run_app(app)
except Exception as e:
    lgr.exception(e)

