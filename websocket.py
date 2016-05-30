import asyncio

from aiohttp.web import WebSocketResponse, MsgType


@asyncio.coroutine
def websocket_handler(request):
    resp = WebSocketResponse()
    yield from resp.prepare(request)
    request.app['sockets'].append(resp)
    resp.send_str("connected")
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

