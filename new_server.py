import argparse
import logging.handlers
import aiohttp_jinja2
import jinja2

from server import nordic_serial
from aiohttp import web
from server.app import app
from server.constants import SERIAL_SPEED
from server.handlers import instruction_handler

from server.id_generator import get_id
from server.websocket import websocket_handler

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))


def add_routes(serial):
    # create some routes.
    app.router.add_route('POST', '/nordic', serial.send_nordic)
    app.router.add_static("/app/", "static/app/")
    app.router.add_route("GET", '/instructions/{lang}', instruction_handler)


def setup_websocket():
    app.router.add_route('GET', '/ws', websocket_handler)
    app['sockets'] = []
    # http://localhost:8080/app/ws.html


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serialport")
    args = parser.parse_args()
    SERIAL_PORT = args.serialport

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    lgr = logging.getLogger()
    lgr.setLevel(logging.WARNING)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    fh = logging.handlers.RotatingFileHandler("logs/nordic.log", 'a', 10000, 5)
    fh.setLevel(logging.INFO)

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    lgr.addHandler(fh)
    lgr.addHandler(ch)

    lgr.info("***** start logging ******")

    network_id = get_id()
#    network_id = b"N"
    serial = nordic_serial.NordicSerial(app.loop, SERIAL_PORT, SERIAL_SPEED, network_id)

    add_routes(serial)
    setup_websocket()
    try:
        web.run_app(app)
    except Exception as e:
        lgr.exception("Some error has occurred.")
