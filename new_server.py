import os
from aiohttp import web

from server.app import get_app
from server.constants import SERIAL_SPEED, STATIC_FILES_FOLDER
from server.mylogger.mylogger import setup_logging

import argparse
import logging.handlers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serialport")
    parser.add_argument("--port", type=int)
    parser.add_argument("--staticfolder")
    parser.add_argument("--instructionsfolder")
    args = parser.parse_args()
    SERIAL_PORT = args.serialport
    WEB_PORT = args.port

    static_files_folder = args.staticfolder
    if not static_files_folder:
        static_files_folder = STATIC_FILES_FOLDER

    instructions_folder = args.instructionsfolder
    if not instructions_folder:
        instructions_folder = os.path.join(STATIC_FILES_FOLDER, 'instructions')

    setup_logging("server/logging.json")
    lgr = logging.getLogger(__name__)
    lgr.info("***** start logging ******")

    app = get_app(
        SERIAL_PORT, SERIAL_SPEED, static_files_folder, instructions_folder)

    try:
        web.run_app(app, port=WEB_PORT)
    except Exception as e:
        lgr.exception("Some error has occurred.")
