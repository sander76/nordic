call git pull
:: assuming the virtualenv is located one folder higher
call ..\..\nordic-venv\scripts\activate.bat
cd ..

python new_server.py