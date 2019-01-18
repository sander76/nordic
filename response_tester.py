import argparse
import asyncio
import logging
from asyncio import coroutine
from unittest.mock import MagicMock

from server.constants import SERIAL_SPEED
from server.id_generator import get_id
from server.nordic import Nd

LOGGER = logging.getLogger(__name__)
#from server.simple_serial import NordicSerial
from server.threaded_serial import NordicSerial
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


def keys():
    _keys = [
        Nd.open,
        Nd.close,
        Nd.stop,
        Nd.CONNECT,
        Nd.STARTPROGRAM,
        Nd.SAVE_POSITION_TOP,
        Nd.STARTPROGRAM,
        Nd.SAVE_POSITION_BOTTOM,
    ]
    for _key in _keys:
        yield Req(_key.name)

def all_keys():
    for en in Nd:
        if not en.name == Nd.SET_DONGLE_ID.name:
            yield Req(en.name)

@asyncio.coroutine
def looper(connector:NordicSerial):
    sleeps = (0.01, 0.001, 0.1, 0.04, 0.2, 0.0001)
    sleep_id = 0

    def get_sleep():
        nonlocal sleep_id
        sleep_id += 1
        if sleep_id == len(sleeps):
            sleep_id = 0
        return sleeps[sleep_id]

    loops = 20
    yield from connector.connect()
    for loop in range(loops):

        LOGGER.info("loop %s", loop)
        # connector.disconnect()
        # yield from asyncio.sleep(1)

        for key in all_keys():
            yield from serial.send_nordic(key)
            slp = get_sleep()
            LOGGER.debug("Sleeping %s", slp)
            yield from asyncio.sleep(slp)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("comport", help="nordic dongle")
    args = parser.parse_args()

    LOGGER.info("Using simple connector")


    serial_port = args.comport

    network_id = get_id()
    loop = asyncio.get_event_loop()
    serial = NordicSerial(loop,serial_port,SERIAL_SPEED,messengers=MagicMock())
    # loop.create_task(looper(serial))
    loop.run_until_complete(looper(serial))
    # loop.run_forever()
