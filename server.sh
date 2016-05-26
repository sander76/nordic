#!/bin/bash

HOME=/home/pi
VENVDIR=$HOME/venv/nordic
BINDIR=$HOME/nordic

source $VENVDIR/bin/activate
$BINDIR/new_server.py
