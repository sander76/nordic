#!/bin/bash

HM=/home/pi

if [ $# -eq 0 ];
    then
        echo "no argument supplied"
    else
        echo "argument supplied"
        HM=$1
fi


VENVDIR=$HM/venv/nordic
BINDIR=$HM/nordic

. $VENVDIR/bin/activate
cd $BINDIR
python new_server.py --serialport="/dev/ttySEGGER"
