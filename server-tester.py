import asyncio
from asyncio import coroutine

import aiohttp

from server.nordic import Nd


commands = [
    [Nd.open.name],
    [Nd.close.name],
    [Nd.stop.name],
    [Nd.CONNECT.name],
    [Nd.STARTPROGRAM.name],
    [Nd.SAVE_POSITION_TOP.name],
    [Nd.STARTPROGRAM.name],
    [Nd.SAVE_POSITION_BOTTOM.name],
]


def _delays():
    _dels = [0.1, 0.5, 0.1, 1, 0.5]
    while True:
        for item in _dels:
            yield item


delays = iter(_delays())


async def looper():
    loop = 50

    async with aiohttp.ClientSession() as session:
        for i in range(loop):
            for command in commands:
                async with session.post(
                    "http://localhost:8080/nordic", json={"commands": command}
                ) as resp:
                    print(resp.text())
                await asyncio.sleep(next(delays))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(looper())
