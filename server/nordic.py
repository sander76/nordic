from collections import namedtuple

class Nordic:
    main_string_id = 0

    def __init__(self, nordic_command):
        self.nordic_command = nordic_command
        self.string_id = None
        self._set_string_id()

    def _set_string_id(self):
        self.string_id = "i{}".format(Nordic.main_string_id)
        Nordic.main_string_id += 1


OPEN = Nordic(b'\x00\x03RU\x00')
CLOSE = Nordic(b'\x00\x03RD\x00')
TILT_OPEN = Nordic(b'\x00\x03RR\x00')
TILT_CLOSE = Nordic(b'\x00\x03RL\x00')
STOP = Nordic(b'\x00\x03RS\x00')
JOG = Nordic(b'\x00\x03cj.1')
CONNECT = Nordic(b'\x00\x01N\x00\x01A')
NETWORKADD = Nordic(b'\x00\x01N')
GROUP_ADD = Nordic(b'\x00\x01A')
RESET = Nordic(b'\x00\x03#@r')
ROLLER = Nordic(b'\x00\x04#DS*')
TWIST = Nordic(b'\x00\x04#DS,')
STARTPROGRAM = Nordic(b'\x00\x04#LPE')
SAVE_POSITION_TOP = Nordic(b'\x00\x04#LPO')
SAVE_POSITION_BOTTOM = Nordic(b'\x00\x04#LPC')
ENABLE_SLAT = Nordic(b'\x00\x04#LPr')
SAVE_SLAT_OPEN = Nordic(b'\x00\x04#LTO')
REVERSE = Nordic(b'\x00\x02#x')
M25S_VENETIAN_16MM = Nordic(b'\x00\x04#DS>')
M25S_VENETIAN_25MM = Nordic(b'\x00\x04#DS~')

BACKROLLER_LEFT = Nordic(b'\x00\x03#dL')  # works with venetian M25S too
BACKROLLER_RIGHT = Nordic(b'\x00\x03#dR')  # works with venetian M25S too
SAVE_VENETIAN_SLAT = Nordic(b'\x00\x04#LPR')
M25S_PLEATED_FREE = Nordic(b'\x00\x04#DS\x11')
M25S_PLEATED_TENSIONED = Nordic(b'\x00\x04#DSQ')
M25S_DUETTE_FREE = Nordic(b'\x00\x04#DS\x06')
M25S_DUETTE_TENSIONED = Nordic(b'\x00\x04#DSF')

# motor types.
M25S_VVB_LEFT_STACK = Nordic(b'\x00\x04#DS6')
M25S_VVB_RIGHT_STACK = Nordic(b'\x00\x04#DS7')
M25S_VVB_SPLIT_STACK = Nordic(b'\x00\x04#DS8')
M25S_VVB_CENTER_STACK = Nordic(b'\x00\x04#DS?')

# motor orientations.
M25S_VVB_LEFT = Nordic(b'\x00\x03#dR')
M25S_VVB_RIGHT = Nordic(b'\x00\x03#dL')
M25S_VVB_CENTER = Nordic(b'\x00\x03#dC')
M25S_VVB_UPRIGHT_LEFT = Nordic(b'\x00\x03#d\xB6')
M25S_VVB_UPRIGHT_RIGHT = Nordic(b'\x00\x03#d\xB0')
M25S_VVB_UPRIGHT_CENTER = Nordic(b'\x00\x03#d\xA7')

