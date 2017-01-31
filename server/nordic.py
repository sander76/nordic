OPEN = "open"
CLOSE = "close"
TILT_OPEN = "tiltopen"
TILT_CLOSE = "tiltclose"
STOP = "stop"
JOG = "jog"
STARTPROGRAM = "startprogram"
SAVE_POSITION_TOP = "savepositiontop"
BACKROLLER_LEFT = "backroller_left"
BACKROLLER_RIGHT = "backroller_right"
CONNECT = "connect"
NETWORKADD = "networkadd"
GROUP_ADD = "group1add"
RESET = "reset"
ROLLER = "roller"  # stopped here
TWIST = "twist"
SAVE_POSITION_BOTTOM = "savepositionbottom"
ENABLE_SLAT = "enableslat"
SAVE_SLAT_OPEN = "saveslatopen"
REVERSE = "reverse"
M25S_VENETIAN_16MM = "m25s_venetian_16mm"
M25S_VENETIAN_25MM = "m25s_venetian_25mm"
SAVE_VENETIAN_SLAT = "save_venetian_slat"
M25S_PLEATED_FREE = "m25s_pleated_free"
M25S_PLEATED_TENSIONED = "m25s_pleated_tensioned"
M25S_DUETTE_FREE = "m25s_duette_free"
M25S_DUETTE_TENSIONED = "m25s_duette_tensioned"

COMMANDS = {
    OPEN: b'\x00\x03RU\x00',
    CLOSE: b'\x00\x03RD\x00',
    TILT_OPEN: b'\x00\x03RR\x00',
    TILT_CLOSE: b'\x00\x03RL\x00',
    STOP: b'\x00\x03RS\x00',
    JOG: b'\x00\x03cj.1',
    CONNECT: b'\x00\x01N\x00\x01A',
    NETWORKADD: b'\x00\x01N',
    GROUP_ADD: b'\x00\x01A',
    RESET: b'\x00\x03#@r',
    ROLLER: b'\x00\x04#DS*',
    TWIST: b'\x00\x04#DS,',
    STARTPROGRAM: b'\x00\x04#LPE',
    SAVE_POSITION_TOP: b'\x00\x04#LPO',
    SAVE_POSITION_BOTTOM: b'\x00\x04#LPC',
    ENABLE_SLAT: b'\x00\x04#LPr',
    SAVE_SLAT_OPEN: b'\x00\x04#LTO',
    REVERSE: b'\x00\x02#x',
    M25S_VENETIAN_16MM: b'\x00\x04#DS>',
    M25S_VENETIAN_25MM: b'\x00\x04#DS~',
    BACKROLLER_LEFT: b'\x00\x03#dL',  # works with venetian M25S too
    BACKROLLER_RIGHT: b'\x00\x03#dR',  # works with venetian M25S too
    SAVE_VENETIAN_SLAT: b'\x00\x04#LPR',
    M25S_PLEATED_FREE: b'\x00\x04#DS\x11',
    M25S_PLEATED_TENSIONED: b'\x00\x04#DSQ',
    M25S_DUETTE_FREE: b'\x00\x04#DS\x06',
    M25S_DUETTE_TENSIONED: b'\x00\x04#DSF'
}
#
# COMMANDS = {
#     "open": {"up": b'\x00\x03RU\x00', "down": b'\x03\RU\x00'},
#     "close": {"up": b'\x00\x03RD\x00'},
#     "tiltopen": {"up": b'\x00\x03RR\x00'},
#     "tiltclose": {"up": b'\x00\x03RL\x00'},
#     "stop": {"up": b'\x00\x03RS\x00'},
#     "jog": {"up": b'\x00\x03cj.1'},
#     "connect": {"up": b'\x00\x01N\x00\x01A'},  # a network add and a add group 1 command combined.
#     "networkadd": {"up": b'\x00\x01N'},
#     "group1add": {"up": b'\x00\x01A'},
#     "reset": {"up": b'\x00\x03#@r'},
#     "roller": {"up": b'\x00\x04#DS*'},
#     "twist": {"up": b'\x00\x04#DS,'},
#     "startprogram": {"up": b'\x00\x04#LPE'},
#     "savepositiontop": {"up": b'\x00\x04#LPO'},
#     "savepositionbottom": {"up": b'\x00\x04#LPC'},
#     "saveslatopen": {"up": b'\x00\x04#LTO'},
#     "reverse": {"up": b'\x00\x02#x'}
# }

if __name__ == "__main__":
    import argparse
    from serial import Serial

    parser = argparse.ArgumentParser()
    parser.add_argument("serialport", help="provide a serial port.")

    args = parser.parse_args()
    SERIAL_PORT = args.serialport
    SERIAL_SPEED = 38400
    s = Serial(SERIAL_PORT, SERIAL_SPEED)
    commands = {"o": ("open", COMMANDS["open"]),
                "c": ("close", COMMANDS["close"])}
    print("************************************")
    for key, value in commands.items():
        print("{:<10}:{}".format(value[0], key))
    print("")
    print("quit  : 'q'")
    print("************************************")
    print("enter a key")
    while 1:
        inp = input()
        if inp == "q":
            break
        val = commands.get(inp)
        if val is not None:
            s.write(val[1])
    s.close()
