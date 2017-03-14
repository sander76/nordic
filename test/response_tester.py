# serial = nordic_serial.NordicSerial(app.loop, SERIAL_PORT, SERIAL_SPEED, network_id)
import asyncio
import logging
import argparse

from server import nordic
from server.messenger import Messengers

from server.constants import SERIAL_SPEED
from server.id_generator import get_id

from server.nordic import COMMANDS
from server.nordic_serial import NordicSerial


def keys():
    _keys = (nordic.OPEN, nordic.CLOSE, nordic.STOP,
             b'\x00\x03RU')
    i = 0
    for _key in _keys:
        yield _key


@asyncio.coroutine
def looper(loop, serial_port):
    loops = 1
    messengers = Messengers(loop)
    serial = NordicSerial(loop, serial_port, SERIAL_SPEED, network_id,
                          messengers=messengers)
    while loops < 50:
        loops += 1
        for key in keys():
            upstring = COMMANDS[key]
            yield from serial.send_queue.put(upstring)
            # print("queue size: {}".format(serial.send_queue.qsize()))
            yield from asyncio.sleep(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--serialport")
    args = parser.parse_args()
    SERIAL_PORT = args.serialport

    logging.basicConfig(level=logging.DEBUG)
    network_id = get_id()
    loop = asyncio.get_event_loop()

    # loop.create_task(looper(serial))
    loop.run_until_complete(looper(loop, SERIAL_PORT))
    # loop.run_forever()
