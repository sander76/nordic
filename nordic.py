from serial import Serial

COMMANDS = {
    "open": b'\x00\x03RU\x00',
    "close": b'\x00\x03RD\x00'
}

if __name__ == "__main__":
    SERIAL_PORT = "COM2"
    SERIAL_SPEED = 38400
    s = Serial(SERIAL_PORT, SERIAL_SPEED)
    commands = {"o": ("open",COMMANDS["open"]),
                "c":("close",COMMANDS["close"])}
    print("************************************")
    for key,value in commands.items():
        print("{:<10}:{}".format(value[0],key) )
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
