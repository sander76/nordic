from aiohttp import web

from server.messenger import Messengers
from server.messenger.web_socket_messenger import WebSocketMessenger
from server.nordic_serial import NordicSerial
from server.webserver.routes import add_routes


def get_app(serial_port, serial_speed):
    app = web.Application()

    ws_messenger = WebSocketMessenger(app)
    messengers = Messengers(app)
    messengers.messengers.append(ws_messenger)

    serial = NordicSerial(
        app.loop, serial_port, serial_speed, messengers=messengers)
    app['serial'] = serial
    app['sockets'] = []

    add_routes(app, serial)

    return app
