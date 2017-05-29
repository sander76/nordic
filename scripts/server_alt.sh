#!/bin/bash

HOME=/home/ecmenc
VENVDIR=$HOME/venv_nordic/
BINDIR=$HOME/nordic

source $VENVDIR/bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttyUSB0"
