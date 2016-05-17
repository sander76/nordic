import asyncio
import concurrent
import time
from aiohttp import web
from serial import Serial
from nordic import COMMANDS
from helpers import view_factory
# Normal serial blocking reads
# This could also do any processing required on the data
from websocket import websocket_handler
#from async_serial import get_and_print

SERIAL_PORT = "COM11"
SERIAL_SPEED = 38400
s = Serial(SERIAL_PORT, SERIAL_SPEED)
app = web.Application()
loop = app.loop

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
        #print(msg)
        send_socket_message(msg)

task = asyncio.Task(get_and_print())


def send_socket_message(message):
    for ws in app['sockets']:
        ws.send_str(message)


def send_nordic(request):
    rq = yield from request.json()
    command = rq['command']
    upstring = COMMANDS.get(command)
    if upstring is not None:
        s.write(upstring)
        return web.Response(body="okay")
    else:
        return web.Response(body="not okay",status=500)


app.router.add_route('POST', '/nordic', send_nordic)
app.router.add_route("GET", '/app/', view_factory('/', 'static/app/index.html'))
app.router.add_static("/app/", "static/app/")
# add the websocket address
app.router.add_route('GET', '/ws', websocket_handler)
# keep a list with all websocket connections.
app['sockets'] = []

web.run_app(app)
