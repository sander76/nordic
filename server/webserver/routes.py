from server.webserver.views import instruction_handler, websocket_handler, \
    get_connection_status


def add_routes(app, serial):
    # create some routes.
    app.router.add_route('POST', '/nordic', serial.send_nordic)
    app.router.add_static("/app/", "static/app/")
    app.router.add_route("GET", '/instructions/{lang}', instruction_handler)
    app.router.add_route('GET', '/ws', websocket_handler)
    app.router.add_route("GET","/serialstatus/status",get_connection_status)
