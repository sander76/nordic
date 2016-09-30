import json
import asyncio
from aiohttp import web
import logging

lgr=logging.getLogger(__name__)

# @asyncio.coroutine
# def instruction_handler(request):
#     lang = request.match_info.get('lang', 'en')
#     fl = "instructions-{}.json".format(lang)
#     try:
#         lgr.info("opening from default location.")
#         with open("/static/app/instructions/{}".format(fl)) as fl:
#             _js = json.load(fl)
#     except FileNotFoundError as e:
#         lgr.info("file not found. Now checking custom location.")
#         with open("/custom_instructions/{}".format(fl)) as fl:
#             _js = json.load(fl)
#
#     return web.json_response(_js)
    #return aiohttp.web.HTTPFound("/app/instructions/{}".format(fl))


