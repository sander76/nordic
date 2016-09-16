import logging

lgr = logging.getLogger(__name__)

class BaseMessenger:
    def send_message(self,message):
        lgr.info("sending message: {}".message)


class Messengers(list):
    def send_message(self,message):
        for messenger in self:
            messenger.send_message(message)
