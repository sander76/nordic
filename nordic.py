from serial import Serial
import argparse

COMMANDS = {
    "open": b'\x00\x03RU\x00',
    "close": b'\x00\x03RD\x00'
}

parser = argparse.ArgumentParser()
parser.add_argument("serialport",help="provide a serial port.")

if __name__ == "__main__":
    args = parser.parse_args()
    SERIAL_PORT = args.serialport
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
    s.close()
