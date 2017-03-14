from aiohttp import web

from server.app import get_app
from server.constants import SERIAL_SPEED
from server.mylogger.mylogger import setup_logging

import argparse
import logging.handlers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serialport")
    parser.add_argument("--port", type=int)
    args = parser.parse_args()
    SERIAL_PORT = args.serialport
    WEB_PORT = args.port

    setup_logging("server/logging.json")
    lgr = logging.getLogger(__name__)
    lgr.info("***** start logging ******")

    app = get_app(SERIAL_PORT, SERIAL_SPEED)

    try:
        web.run_app(app, port=WEB_PORT)
    except Exception as e:
        lgr.exception("Some error has occurred.")
