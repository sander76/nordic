# serial = nordic_serial.NordicSerial(app.loop, SERIAL_PORT, SERIAL_SPEED, network_id)
import asyncio
import logging
logging.basicConfig(level=logging.DEBUG)

from server.constants import SERIAL_SPEED
from server.id_generator import get_id
from server.nordic import COMMANDS
from server.nordic_serial import NordicSerial




def keys():
    _keys = list(COMMANDS.keys())
    i = 0
    while 1:
        yield _keys[i]
        i += 1
        if i >= len(_keys):
            i = 0


@asyncio.coroutine
def looper():
    serial = NordicSerial(loop, "COM4", SERIAL_SPEED, network_id)
    while 1:
        if serial.s.is_open:
            for key in keys():
                upstring = COMMANDS[key]
                serial._write_to_nordic(upstring)
                yield from asyncio.sleep(10)
        else:
            logging.debug("retrying in 5 seconds.")
            yield from asyncio.sleep(5)


if __name__ == "__main__":
    network_id = get_id()
    loop = asyncio.get_event_loop()

    #loop.create_task(looper(serial))
    loop.run_until_complete(looper())
    #loop.run_forever()
