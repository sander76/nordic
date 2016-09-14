#!/bin/bash

HOME=/home/pi
VENVDIR=$HOME/venv/nordic
BINDIR=$HOME/nordic

source $VENVDIR/bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttyACM0"
