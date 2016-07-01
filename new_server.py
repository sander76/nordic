import logging
import logging.handlers
import argparse
import nordic_serial
# import asyncio

import aiohttp_jinja2
import jinja2
from aiohttp import web
from app import app
from constants import SERIAL_SPEED
from websocket import websocket_handler


@aiohttp_jinja2.template('index.html')
def index_handler(request):
    # Get the language part of the url. Defaults to "en" english.
    lang = request.match_info.get('lang', 'en')
    return {'lang': lang}


parser = argparse.ArgumentParser()
parser.add_argument("--serialport")
args = parser.parse_args()

SERIAL_PORT = args.serialport

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))


def add_routes(serial):
    # create some routes.
    app.router.add_route('POST', '/nordic', serial.send_nordic)
    app.router.add_static("/app/", "static/app/")
    app.router.add_route("GET", '/site/{lang}/', index_handler)


def setup_websocket():
    app.router.add_route('GET', '/ws', websocket_handler)
    app['sockets'] = []
    # http://localhost:8080/app/ws.html


if __name__ == "__main__":
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    lgr = logging.getLogger()
    lgr.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.handlers.RotatingFileHandler("logs/nordic.log", 'a', 10000, 5)
    fh.setLevel(logging.INFO)

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    lgr.addHandler(fh)
    lgr.addHandler(ch)

    lgr.info("***** start logging ******")
    serial = nordic_serial.NordicSerial(app.loop, SERIAL_PORT, SERIAL_SPEED)
    add_routes(serial)
    setup_websocket()
    try:
        web.run_app(app)
    except Exception as e:
        lgr.exception("Some error has occurred.")
