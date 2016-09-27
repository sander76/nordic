#!/bin/bash

#this will update the PowerView programmer from github
cd ~/nordic
git checkout release
git pull

sudo systemctl restart nordic
#echo "please restart you computer"

$SHELL