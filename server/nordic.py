COMMANDS = {
    "open": b'\x00\x03RU\x00',
    "close": b'\x00\x03RD\x00',
    "tiltopen": b'\x00\x03RR\x00',
    "tiltclose": b'\x00\x03RL\x00',
    "stop": b'\x00\x03RS\x00',
    "jog": b'\x00\x03cj.1',
    "connect": b'\x00\x01N\x00\x01A',  # a network add and a add group 1 command combined.
    "networkadd": b'\x00\x01N',
    "group1add": b'\x00\x01A',
    "reset": b'\x00\x03#@r',
    "roller": b'\x00\x04#DS*',
    "twist": b'\x00\x04#DS,',
    "startprogram": b'\x00\x04#LPE',
    "savepositiontop": b'\x00\x04#LPO',
    "savepositionbottom": b'\x00\x04#LPC',
    "saveslatopen":b'\x00\x04#LTO',
    "reverse": b'\x00\x02#x',
    "m25s_venetian_16mm":b'\x00\x04#DS\x14',
    "m25s_venetian_25mm":b'\x00\x04#DST'

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
