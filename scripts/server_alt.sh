#!/bin/bash

HOME=/home/ecmenc

VENVDIR=$HOME/venv_nordic/
BINDIR=$HOME/nordic

cd $VENVDIR
source bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttyUSB0"
