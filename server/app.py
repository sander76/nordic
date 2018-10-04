import asyncio
from aiohttp import web

from server.messenger import Messengers
from server.messenger.web_socket_messenger import WebSocketMessenger
from server.simple_serial import NordicSerial
# from server.nordic_serial import NordicSerial
from server.webserver.routes import add_routes


def get_app(serial_port, serial_speed, static_folder, instructions_folder):
    app = web.Application(loop=asyncio.get_event_loop())

    ws_messenger = WebSocketMessenger(app)
    messengers = Messengers(app)
    messengers.messengers.append(ws_messenger)

    serial = NordicSerial(
        app.loop, serial_port, serial_speed, messengers=messengers)

    app['serial'] = serial
    app['sockets'] = []

    add_routes(app, serial, static_folder, instructions_folder)

    return app
