# creates a windows startup file.

with open("startup.bat", 'w') as fl:
    fl.write('cd..\n')
    fl.write('call git pull\n')

    fl.write('call env\\scripts\\activate.bat\n')
    serial_port = input("Provide serial port of dongle: ")
    fl.write('python new_server.py --serialport="{}"\n'.format(serial_port))
