import asyncio

class FakeSerial():
    def __init__(self):
        pass

    def read(self,charcount):
        while 1:
            yield from asyncio.sleep(10)

    def write(self,bytes):
        pass
