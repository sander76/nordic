import asyncio
import logging

from asyncio import coroutine
from unittest.mock import Mock, MagicMock

from server.nordic import Nd
from server.messenger import Messengers

from server.constants import SERIAL_SPEED
from server.id_generator import get_id


LOGGER = logging.getLogger(__name__)
#from server.simple_serial import NordicSerial
from server.nordic_serial import NordicSerial


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


@asyncio.coroutine
def looper(loop, serial_port):
    sleeps = (0.1, 1, 3, 0.4, 0.2, 0.01)
    sleep_id = 0

    def get_sleep():
        nonlocal sleep_id
        sleep_id += 1
        if sleep_id == len(sleeps):
            sleep_id = 0
        return sleeps[sleep_id]

    loops = 1
    # messengers = Messengers(loop)
    serial = NordicSerial(
        loop, serial_port, SERIAL_SPEED, network_id, messengers=MagicMock()
    )

    #serial.connect()

    while loops < 150:
        LOGGER.debug("loop %s", loops)
        loops += 1
        for key in keys():
            yield from serial.send_nordic(key)
            slp = get_sleep()
            LOGGER.debug("Sleeping %s", slp)
            yield from asyncio.sleep(slp)


if __name__ == "__main__":
    serial_port = "COM15"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    network_id = get_id()
    loop = asyncio.get_event_loop()

    # loop.create_task(looper(serial))
    loop.run_until_complete(looper(loop, serial_port))
    # loop.run_forever()
