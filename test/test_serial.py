import unittest

import asyncio
from unittest.mock import MagicMock

from server.constants import SERIAL_SPEED
from server.id_generator import get_id
from server.nordic_serial import NordicSerial

serial_port = "COM 8"


class TestSerial(unittest.TestCase):
    def setUp(self):
        network_id = get_id()
        loop = asyncio.get_event_loop()
        self.serial = NordicSerial(loop, serial_port, SERIAL_SPEED, network_id,
                                   messengers=MagicMock())
