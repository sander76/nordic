import argparse
import logging.handlers
import jinja2

from server import nordic_serial
from aiohttp import web
from server.app import app
from server.constants import SERIAL_SPEED
# from server.handlers import instruction_handler

from server.id_generator import get_id
from server.messenger import Messengers
from server.mylogger import setup_logging
from server.websocket import websocket_handler, WebSocketMessenger
import asyncio
import json


# @asyncio.coroutine
def instruction_handler(request):
    lang = request.match_info.get('lang', 'en')
    fl = "instructions-{}.json".format(lang)
    try:
        lgr.info("opening from default location.")
        with open("static/app/instructions/{}".format(fl)) as fl:
            _js = json.load(fl)
    except FileNotFoundError as e:
        lgr.info("file not found. Now checking custom location.")
        with open("custom_instructions/{}".format(fl)) as fl:
            _js = json.load(fl)
    return web.json_response(_js)


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
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    SERIAL_PORT = args.serialport
    port = args.port

    setup_logging("server/logging.json")
    lgr = logging.getLogger(__name__)
    lgr.info("***** start logging ******")

    network_id = get_id()
    #    network_id = b"N"
    ws_messenger = WebSocketMessenger()
    messengers = Messengers(app.loop)
    messengers.messengers.append(ws_messenger)
    serial = nordic_serial.NordicSerial(
        app.loop, SERIAL_PORT, SERIAL_SPEED, network_id, messengers=messengers)

    add_routes(serial)
    setup_websocket()
    try:
        web.run_app(app, port=port)
    except Exception as e:
        lgr.exception("Some error has occurred.")
