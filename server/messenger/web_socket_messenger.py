import asyncio
import json

from server.messenger import BaseMessenger


class WebSocketMessenger(BaseMessenger):
    @asyncio.coroutine
    def send_message(self, message):
        yield from self.send_socket_message(message)

    @asyncio.coroutine
    def send_socket_message(self, message):
        for ws in self.app['sockets']:
            yield from ws.send_str(json.dumps(message))
