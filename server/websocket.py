import asyncio
import json

from aiohttp.web import WebSocketResponse, MsgType

from server.app import app
from server.messenger import BaseMessenger


class WebSocketMessenger(BaseMessenger):
    @asyncio.coroutine
    def send_message(self, message):
        yield from self.send_socket_message(message)

    @asyncio.coroutine
    def send_socket_message(self,message):
        for ws in app['sockets']:
            ws.send_str(json.dumps(message))


@asyncio.coroutine
def websocket_handler(request):
    resp = WebSocketResponse()
    yield from resp.prepare(request)
    request.app['sockets'].append(resp)
    #resp.send_str("connected")
    while True:
        msg = yield from resp.receive()
        if msg.tp == MsgType.text:
            for ws in request.app['sockets']:
                if ws is not resp:
                    ws.send_str(msg.data)
        else:
            break
    request.app["sockets"].remove(resp)
    return resp

