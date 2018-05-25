import logging
import asyncio

lgr = logging.getLogger(__name__)


class BaseMessenger:
    def __init__(self, app):
        self.app = app

    @asyncio.coroutine
    def send_message(self, message):
        lgr.debug("sending message: {}".format(message))


class Messengers:
    def __init__(self, app):
        #self.messengers = [BaseMessenger(app)]
        self.messengers = []
        self._messages = asyncio.Queue(loop=app.loop)
        app.loop.create_task(self._check_queue())

    @asyncio.coroutine
    def send_message(self, message):
        yield from self._messages.put(message)

    @asyncio.coroutine
    def send_outgoing_data(self, message):
        yield from self._messages.put({"to": str(message)})

    @asyncio.coroutine
    def send_incoming_data(self, message):
        yield from self._messages.put({"from": str(message)})

    @asyncio.coroutine
    def _check_queue(self):
        """continuously check for incoming messages."""
        while 1:
            # check the message queue for messages.
            message = yield from self._messages.get()
            # self._messages.task_done()
            yield from self._send_message(message)

    @asyncio.coroutine
    def _send_message(self, message):
        for messenger in self.messengers:
            yield from messenger.send_message(message)
