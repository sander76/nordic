# serial = nordic_serial.NordicSerial(app.loop, SERIAL_PORT, SERIAL_SPEED, network_id)
import asyncio
import logging

from server.messenger import Messengers

from server.constants import SERIAL_SPEED
from server.id_generator import get_id
import server.nordic
from server.nordic import COMMANDS
from server.nordic_serial import NordicSerial


def keys():
    _keys = (server.nordic.OPEN, server.nordic.CLOSE, server.nordic.STOP)
    i = 0
    for _key in _keys:
        yield _key


@asyncio.coroutine
def looper(loop):
    loops = 1
    messengers = Messengers(loop)
    serial = NordicSerial(loop, "COM8", SERIAL_SPEED, network_id,
                          messengers=messengers)
    while loops < 50:
        loops += 1
        for key in keys():
            upstring = COMMANDS[key]
            yield from serial.send_queue.put(upstring)
            #print("queue size: {}".format(serial.send_queue.qsize()))
            yield from asyncio.sleep(2)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    network_id = get_id()
    loop = asyncio.get_event_loop()

    # loop.create_task(looper(serial))
    loop.run_until_complete(looper(loop))
    # loop.run_forever()
