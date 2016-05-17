from aiohttp import web


def view_factory(url, path):
    """
    Factory method to serve a single
    static file.
    """
    async def static_view(request):
        prefix = url.rsplit('/', 1)[0] or '/'
        route = web.StaticRoute(None, prefix, '')
        request.match_info['filename'] = path
        return await route.handle(request)

    return static_view
