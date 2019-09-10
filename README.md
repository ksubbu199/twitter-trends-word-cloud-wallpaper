# Twitter-Trend-Wallpaper
A python and shell script to set the wallpaper to a wordcloud of the most trending google searches. 

This project is inspired from https://github.com/shardul08/Google-Trend-Wallpaper. You can check it out for the wordcloud of most resource hungry processes running in your system.

![Screenshot](https://github.com/ksubbu199/twitter-trends-word-cloud-wallpaper/blob/master/wallpaper.png)  


## Dependencies
* `python3`
* `gsettings` or `feh`  To set the generated wordcloud as the wallpaper
* `xvfb`  To simulate a display and run everything in memory
### Python dependencies
* `wordcloud` To generate the wordcloud
* `PIL`  Python imaging library

## Setup
* Run `setup.sh` with
```
./setup.sh
```
This will install all the required dependencies and set the wallpaper.
* Add twitter.json file with following entries `consumerKey`,`consumerSecret`,`accessKey`,`accessSecret`

## Usage
Run `./updateWallpaper.sh` to update the wallpaper to the wordcloud of the latest trends.

**NOTE** If the wallpaper is not set automatically, you can set `wallpaper.png` as the wallpaper manually.

If you want the wallpaper to refresh/update every hour, you can add a cron job to run the script every hour.

To add a cron job, run

`crontab -e`

append the following

`0 * * * * cd path/to/script/directory && ./updateWallpaper.sh > /tmp/wallpaper.log > 2>&1`

This will refresh the wallpaper every hour. You can customize this command to refresh the wallpaper as often you want.
