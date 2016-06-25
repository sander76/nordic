import argparse
import asyncio
import concurrent
import json
import time

import aiohttp_jinja2
import jinja2
from aiohttp import web
from serial import Serial
from serial.serialutil import SerialException

from constants import SERIAL_SPEED, SLEEP_BETWEEN_COMMANDS, TRYDELAY, NORDIC_CONNECTED, NORDIC_NOT_CONNECTED
from nordic import COMMANDS

from websocket import websocket_handler
import logging.handlers

lgr = logging.getLogger(__name__)
lgr.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh = logging.handlers.RotatingFileHandler("logs/nordic.log", 'a', 10000, 5)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
fh.setLevel(logging.ERROR)

lgr.addHandler(ch)
lgr.addHandler(fh)


def get_byte():
    while 1:
        if s.is_open:
            data = bytearray(s.read(1))
            time.sleep(0.3)
            data += bytearray(s.read(s.inWaiting()))
            return data
        time.sleep(TRYDELAY)


# Runs blocking function in executor, yielding the result
@asyncio.coroutine
def get_byte_async():
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        res = yield from loop.run_in_executor(executor, get_byte)
        return res


def get_and_print():
    while 1:
        b = yield from get_byte_async()
        from_string(None, b)


task = asyncio.Task(get_and_print())


def send_socket_message(message):
    for ws in app['sockets']:
        ws.send_str(json.dumps(message))


def up_string(cmd, upstring):
    msg = {"to": upstring.decode('utf-8')}
    send_socket_message(msg)
    lgr.info(msg)


def from_string(cmd, downstring):
    msg = {"from": downstring.decode('utf-8')}
    send_socket_message(msg)
    lgr.info(msg)


# handlers.
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
                # get the delay value or use default SLEEP_BETWEEN_COMMANDS
                delay = commands.get("delay", SLEEP_BETWEEN_COMMANDS)
                yield from asyncio.sleep(delay)
            try:
                s.write(upstring)
                up_string(cmd, upstring)
            except SerialException:
                lgr.exception("writing to serial port failure.")
                s.close()
                send_socket_message(NORDIC_NOT_CONNECTED)
                # return web.Response(text="Writing to blind went wrong. Please check cables and USB dongle")
        else:
            lgr.error("sending command {} did not succeed.".format(cmd))
            return web.Response(text="sending command {} did not succeed.".format(cmd), status=500)
    return web.Response(body=b"okay")


@aiohttp_jinja2.template('index.html')
def index_handler(request):
    # Get the language part of the url. Defaults to "en" english.
    lang = request.match_info.get('lang', 'en')
    return {'lang': lang}


parser = argparse.ArgumentParser()
parser.add_argument("--serialport")
args = parser.parse_args()

SERIAL_PORT = args.serialport

s = Serial()
s.port = SERIAL_PORT
s.baudrate = SERIAL_SPEED


# handler
def connect():
    lgr.error("Connecting to serial port: {}".format(SERIAL_PORT))
    attempt = 1
    while True:
        if s.is_open:
            send_socket_message(NORDIC_CONNECTED)
        else:
            try:
                lgr.error("Connecting to serial port. Attempt: {}".format(attempt))
                s.open()
                lgr.error("****************** Connected **************************")
                send_socket_message(NORDIC_CONNECTED)
            except SerialException:
                lgr.exception("serial port opening problem.")
                attempt += 1
                send_socket_message(NORDIC_NOT_CONNECTED)
        yield from asyncio.sleep(TRYDELAY)


task = asyncio.Task(connect())

# create the app instance and get the async loop.
app = web.Application()
loop = app.loop
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# create some routes.
app.router.add_route('POST', '/nordic', send_nordic)
app.router.add_static("/app/", "static/app/")
app.router.add_route("GET", '/site/{lang}/', index_handler)

# add the websocket address
# http://localhost:8080/app/ws.html
app.router.add_route('GET', '/ws', websocket_handler)
# keep a list with all websocket connections.
app['sockets'] = []

lgr.error("***** start logging ******")

try:
    web.run_app(app)
except Exception as e:
    lgr.exception("Some error has occurred.")
