#!/bin/bash

HOME=/home/pi
VENVDIR=$HOME/venv/nordic
BINDIR=$HOME/nordic

. $VENVDIR/bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttySEGGER"
