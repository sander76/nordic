import aiohttp.web
import asyncio

#import aiohttp_jinja2


# @aiohttp_jinja2.template('index.html')
# def index_handler(request):
#     # Get the language part of the url. Defaults to "en" english.
#     lang = request.match_info.get('lang', 'en')
#     return {'lang': lang}


asyncio.coroutine
def instruction_handler(request):
    lang = request.match_info.get('lang', 'en')
    fl = "instructions-{}.json".format(lang)
    return aiohttp.web.HTTPFound("/app/instructions/{}".format(fl))

