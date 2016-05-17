import asyncio

from aiohttp import web

from old.aio_serial import create_connection


class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        print('port opened', transport)
        # transport.serial.rts = False
        transport.write(b'hello world\n')

    def data_received(self, data):
        print('data received', repr(data))
        self.transport.close()

    def connection_lost(self, exc):
        print('port closed')
        asyncio.get_event_loop().stop()

    def pause_writing(self):
        print('pause writing')
        print(self.transport.get_write_buffer_size())

    def resume_writing(self):
        print(self.transport.get_write_buffer_size())
        print('resume writing')


# def write_serial():
#     print(NORDIC.read())

# loop = asyncio.get_event_loop()


def hello(request):
    _app = request.app['serial']
    _app.transport.write(b"aaa")


app = web.Application()
app.router.add_route('GET', '/test', hello)
loop = app.loop
nordic = create_connection(Output, loop, port="COM11", baudrate=384000)
loop.run_until_complete(nordic)
#app['serial']=nordic.transport
# loop.run_forever()
# loop.close()


web.run_app(app)
