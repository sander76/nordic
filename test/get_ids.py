# import server.nordic
# from test.another_stop import get_id
#
# for id in server.nordic.__dict__:
#     print(id)
#

from serial.tools.list_ports import comports

for i in comports():
    print('*****')
    print(i.name)
    print(i.pid)
    print(i.vid)

'4966:4117'
'USB VID:PID=1366:1015 LOCATION=1-1'
