#!/bin/bash

HOME=/home/pi

if [ $# -eq 0 ];
    then
        echo "no argument supplied"
    else
        echo "argument supplied"
        echo "$1"
        HOME= "$1"
fi


VENVDIR=$HOME/venv/nordic
BINDIR=$HOME/nordic

. $VENVDIR/bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttySEGGER"
