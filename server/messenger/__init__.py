import logging
import asyncio

lgr = logging.getLogger(__name__)


class BaseMessenger:
    @asyncio.coroutine
    def send_message(self, message):
        lgr.info("sending message: {}".message)


class Messengers:
    def __init__(self, loop):
        self.messengers = []
        self._messages = asyncio.Queue(loop=loop)
        loop.create_task(self._check_queue())

    @asyncio.coroutine
    def send_message(self, message):
        yield from self._messages.put(message)

    @asyncio.coroutine
    def _check_queue(self):
        """continuously check for incoming messages."""
        while 1:
            # check the message queue for messages.
            message = yield from self._messages.get()
            yield from self._send_message(message)

    @asyncio.coroutine
    def _send_message(self, message):
        for messenger in self.messengers:
            yield from messenger.send_message(message)
