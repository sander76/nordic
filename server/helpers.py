import asyncio
from aiohttp import web


# def up_string(cmd, upstring):
#     msg = {"to": str(upstring)}
#     return msg
#
#
# def from_string(cmd, downstring):
#     msg = {"from": str(downstring)}
#     return msg


def view_factory(url, path):
    """
    Factory method to serve a single
    static file.
    """

    @asyncio.coroutine
    def static_view(request):
        prefix = url.rsplit('/', 1)[0] or '/'
        route = web.StaticRoute(None, prefix, '')
        request.match_info['filename'] = path
        val = yield from route.handle(request)
        return val

    return static_view




