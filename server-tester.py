import asyncio
from asyncio import coroutine

import aiohttp

from server.nordic import Nd


commands = [
    Nd.open,
    Nd.close,
    Nd.stop,
    Nd.CONNECT,
    Nd.STARTPROGRAM,
    Nd.SAVE_POSITION_TOP,
    Nd.STARTPROGRAM,
    Nd.SAVE_POSITION_BOTTOM,
    Nd.ORIENT_VVB_UPRIGHT_LEFT,
    Nd.ORIENT_VVB_UPRIGHT_RIGHT,
]


def _delays():
    _dels = [0.1, 0.5, 0.1, 1, 0.5]
    while True:
        for item in _dels:
            yield item


delays = iter(_delays())


async def w_socket(session):
    async with session.ws_connect("ws://localhost:8080/ws") as ws:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.ERROR:
                break
            else:
                print(msg.data)


async def sender(session):
    loop = 10
    for i in range(loop):
        for command in Nd:
            if (
                not command.name == Nd.NETWORKADD.name
                and not command.name == Nd.CONNECT.name
                and not command.name == Nd.SET_DONGLE_ID.name
            ):
                cmd = [command.name]

                print(command.name)
                async with session.post(
                    "http://localhost:8080/nordic", json={"commands": cmd}
                ) as resp:
                    txt = await resp.text()
                    print(txt)
                await asyncio.sleep(next(delays))


async def looper(loop):

    async with aiohttp.ClientSession() as session:
        _ws = loop.create_task(w_socket(session))
        _sender = loop.create_task(sender(session))
        # await _ws
        await _sender

        await session.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(looper(loop))
