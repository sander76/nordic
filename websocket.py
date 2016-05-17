import asyncio

from aiohttp import web


@asyncio.coroutine
def websocket_handler(request):
    resp = web.WebSocketResponse()
    yield from resp.prepare(request)
    request.app['sockets'].append(resp)
    resp.send_str("connected")
    while True:
        msg = yield from resp.receive()
        for ws in request.app['sockets']:
            if ws is not resp:
                ws.send_str(msg.data)

    return resp

