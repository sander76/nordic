import asyncio
import json
import logging

from aiohttp.web import WebSocketResponse, MsgType
from aiohttp import web

lgr = logging.getLogger(__name__)


@asyncio.coroutine
def instruction_handler(request):
    lang = request.match_info.get('lang', 'en')
    fl = "instructions-{}.json".format(lang)
    try:
        lgr.info("opening from default location.")
        with open("static/app/instructions/{}".format(fl)) as fl:
            _js = json.load(fl)
    except FileNotFoundError:
        lgr.info("file not found. Now checking custom location.")
        with open("custom_instructions/{}".format(fl)) as fl:
            _js = json.load(fl)
    return web.json_response(_js)


@asyncio.coroutine
def websocket_handler(request):
    resp = WebSocketResponse()
    yield from resp.prepare(request)
    request.app['sockets'].append(resp)
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

@asyncio.coroutine
def get_connection_status(request):
    status = request.app['serial'].get_connection_status()

    return web.json_response(status)