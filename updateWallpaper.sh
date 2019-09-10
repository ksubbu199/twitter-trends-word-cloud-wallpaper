#!/bin/bash

echo "Creating wallpaper..."
nice python3 generateWallpaper.py
retVal=$?

if [ $retVal -eq 0 ]; then
    sh setWallpaper.sh
else
    echo "Something went wrong"
    echo "You can raise an issue at https://github.com/ksubbu199/twitter-trends-word-cloud-wallpaper/issues"
fi
