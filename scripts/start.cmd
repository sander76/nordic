cd ..
call git pull
call venv\scripts\activate.bat

python new_server.py --serial_discover
