#!/bin/bash

#this will update the PowerView programmer from github

echo "Checking online for new releases"
cd ~/nordic
git checkout release
git pull

echo "Clearing browser cache"
rm -rf ~/.cache/chromium/Default

echo "Restarting Nordic server"
sudo systemctl restart nordic
echo "Finished. You can now close this window."

echo "Shutting down browser"
pkill --oldest chromium
# echo "Restarting browser"
# chromium-browser --start-fullscreen &

$SHELL