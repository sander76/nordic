import argparse
import asyncio
import logging
from asyncio import coroutine
from time import sleep
from unittest.mock import MagicMock
from serial import Serial
from server.constants import SERIAL_SPEED
from server.id_generator import get_id
from server.nordic import Nd

LOGGER = logging.getLogger(__name__)


# from server.simple_serial import NordicSerial
# from server.nordic_serial import NordicSerial


class Req:
    def __init__(self, cmd):
        self.cmd = cmd
        self.str = {"commands": [cmd]}

    @coroutine
    def json(self):
        return self.str


# def to_str(nd_command):
#     comm = {"commands": [{"value": nd_command}]}
#     return json.dumps(comm)



keys = [
        Nd.open,
        Nd.close,
        Nd.stop,
        Nd.CONNECT,
        Nd.STARTPROGRAM,
        Nd.SAVE_POSITION_TOP,
        Nd.STARTPROGRAM,
        Nd.SAVE_POSITION_BOTTOM,
    ]

def get_sleep():
    sleeps = (0.01, 0.001, 0.1, 0.04, 0.2, 0.0001)

    while True:
        for sleep in sleeps:
            yield sleep

def looper(serial_port):
    sleeper = iter(get_sleep())

    loops = 1

    ser = Serial(serial_port,SERIAL_SPEED)

    while loops < 150:
        LOGGER.info("loop %s",loops)

        loops+=1
        for key in Nd:
            if not key.name == Nd.SET_DONGLE_ID.name:
                LOGGER.debug("writing: %s",key)
                ser.write(key.value)
                sleep(0.1)
                LOGGER.debug("reading")
                resp = ser.read(1)
                sleep(0.1)

                resp += ser.read(ser.in_waiting)
                LOGGER.debug("response: %s",resp)

                wait = next(sleeper)
                LOGGER.debug("sleeping %s",wait)
                sleep(next(sleeper))


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("comport", help="nordic dongle")
    parser.add_argument("--simple", dest="simple", action="store_true")
    args = parser.parse_args()

    serial_port = args.comport
    try:
        looper(serial_port)
    except KeyboardInterrupt:
        print("finishing")