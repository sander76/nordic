import asyncio
import concurrent
import time
import argparse

from aiohttp import web
from serial import Serial

from helpers import view_factory
from nordic import COMMANDS

# Normal serial blocking reads
# This could also do any processing required on the data
from websocket import websocket_handler

# from async_serial import get_and_print
#SERIAL_PORT = "COM11"
SERIAL_SPEED = 38400
SLEEP_BETWEEN_COMMANDS = 5



def get_byte():
    data = bytearray(s.read(1))
    time.sleep(0.5)
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
        msg = repr(b)
        print(msg)
        send_socket_message(msg)


task = asyncio.Task(get_and_print())


def send_socket_message(message):
    for ws in app['sockets']:
        ws.send_str(message)


def send_nordic(request):
    rq = yield from request.json()
    #command = rq['command']
    commands = rq['commands']
    first = True
    for cmd in commands:
        upstring = COMMANDS.get(cmd)
        if upstring is not None:
            if first:
                first = False
            else:
                yield from asyncio.sleep(SLEEP_BETWEEN_COMMANDS)
            s.write(upstring)

                #
        else:
            return web.Response(body=b"not okay", status=500)
    return web.Response(body=b"okay")
            # upstring = COMMANDS.get(command)
            # if upstring is not None:
            #     s.write(upstring)
            #     return web.Response(body=b"okay")
            # else:
            #     return web.Response(body=b"not okay", status=500)

parser = argparse.ArgumentParser()
parser.add_argument("serialport")
args=parser.parse_args()

SERIAL_PORT=args.serialport

s = Serial(SERIAL_PORT, SERIAL_SPEED)
app = web.Application()
loop = app.loop

app.router.add_route('POST', '/nordic', send_nordic)
app.router.add_route("GET", '/app/', view_factory('/', 'static/app/index.html'))
app.router.add_static("/app/", "static/app/")
# add the websocket address
app.router.add_route('GET', '/ws', websocket_handler)
# keep a list with all websocket connections.
app['sockets'] = []

web.run_app(app)