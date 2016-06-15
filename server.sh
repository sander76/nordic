#!/bin/bash

HOME=/home/pi
VENVDIR=$HOME/venv/nordic
BINDIR=$HOME/nordic

source $VENVDIR/bin/activate
cd BINDIR
$BINDIR/new_server.py
