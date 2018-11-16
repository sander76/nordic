cd ..
call git pull
call venv\scripts\activate.bat
call pip install -r requirements.txt
python new_server.py --serial_discover
