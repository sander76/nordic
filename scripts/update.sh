#!/bin/bash

#this will update the PowerView programmer from github


cd ~/nordic
echo "Removing network id."
rm network_id.json
echo "Checking online for new releases"
git checkout release
git pull

echo "updating dependencies"
. ~/venv/nordic/bin/activate
pip install -r requirements.txt
deactivate

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