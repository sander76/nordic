import argparse
import logging.handlers

from aiohttp import web
from serial.tools.list_ports import comports

from server.app import get_app
from server.constants import SERIAL_SPEED, STATIC_FILES_FOLDER, \
    INSTRUCTIONS_FOLDER
from server.mylogger.mylogger import setup_logging

PRINT_LENGTH = 80

ATTR_VID = 'vid'
ATTR_PID = 'pid'
ATTR_NAME = 'name'

dongles = [
    {ATTR_VID: 1027, ATTR_PID: 24597, ATTR_NAME: 'Bremerhave dongle'},
    {ATTR_VID: 4966, ATTR_PID: 4117, ATTR_NAME: 'Nordic dongle'}
]

setup_logging("server/logging.json")
lgr = logging.getLogger(__name__)
lgr.info("***** start logging ******")


def get_serial_port():
    for i in comports():
        for _dongle in dongles:
            if i.pid == _dongle[ATTR_PID] and i.vid == _dongle[ATTR_VID]:
                lgr.info("Serial port found. vid: %s pid: %s name: %s", i.pid,
                         i.vid, i.device)
                return i
    print("*" * PRINT_LENGTH)
    print("Unable to discover the correct serial port.")
    print("Is it plugged in? If so please contact support.")
    print("Stopping the program.")
    print("*" * PRINT_LENGTH)
    return False


def print_instructions():
    print("*" * PRINT_LENGTH)
    print("Server running")
    print("Open your CHROME browser and navigate to:")
    print("")
    print("localhost:8080/app/index.html#instructions/all-en/0")
    print("*" * PRINT_LENGTH)


def start_app(serial_port,
              serial_speed=SERIAL_SPEED,
              static_files_folder=STATIC_FILES_FOLDER,
              instructions_folder=INSTRUCTIONS_FOLDER):
    print_instructions()
    app = get_app(serial_port, serial_speed, static_files_folder,
                  instructions_folder)
    try:
        web.run_app(app)
    except Exception as err:
        lgr.exception(err)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serialport")
    parser.add_argument("--port", type=int)
    parser.add_argument("--staticfolder", default=STATIC_FILES_FOLDER)
    parser.add_argument("--instructionsfolder", default=INSTRUCTIONS_FOLDER)
    parser.add_argument("--serial_discover", dest='autodiscover',
                        action='store_true')

    parser.set_defaults(autodiscover=False)
    args = parser.parse_args()

    SERIAL_PORT = None
    if args.autodiscover:
        _serial = get_serial_port()
        if _serial:
            SERIAL_PORT = _serial.device
        else:
            input("Enter to exit")
            exit()
    else:
        SERIAL_PORT = args.serialport

    WEB_PORT = args.port

    static_files_folder = args.staticfolder
    instructions_folder = args.instructionsfolder



    start_app(SERIAL_PORT, SERIAL_SPEED, static_files_folder,
              instructions_folder)
