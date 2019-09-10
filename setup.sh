#!/bin/bash

echo "Installing Python dependencies..."

if ! dpkg-query -W -f='${Status}' xvfb | grep "ok installed"; then sudo apt install xvfb; fi

pillow="$(python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("Pillow") else 0)')"
wordcloud="$(python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("wordcloud") else 0)')"
matplotlib="$(python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("matplotlib") else 0)')"
selenium="$(python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("selenium") else 0)')"
pyvirtualdisplay="$(python3 -c 'import pkgutil; print(1 if pkgutil.find_loader("pyvirtualdisplay") else 0)')"
if [ $pillow == 0 ]; then
echo "Installing Pillow..."
pip3 install --user Pillow
fi
if [ $wordcloud == 0 ]; then
echo "Installing wordcloud..."
pip3 install --user wordcloud
fi

echo "Setup successfully completed"

sh updateWallpaper.sh
