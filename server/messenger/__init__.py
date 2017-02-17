import logging
from asyncio import Queue

lgr = logging.getLogger(__name__)


class BaseMessenger:
    def send_message(self, message):
        lgr.info("sending message: {}".message)


class Messengers:
    def __init__(self, loop):
        self.messengers = []
        self.messages = Queue(loop=loop)

    def send_message(self, message):
        for messenger in self:
            messenger.send_message(message)
