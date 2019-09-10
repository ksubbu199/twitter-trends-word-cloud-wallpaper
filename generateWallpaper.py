import tweepy
from PIL import Image
from wordcloud import WordCloud
import json
import os
import random
import sys


twitterConfig = json.loads(open("twitter.json", "r").read())


consumerKey = twitterConfig["consumerKey"]
consumerSecret = twitterConfig["consumerSecret"]
accessKey = twitterConfig["accessKey"]
accessSecret = twitterConfig["accessSecret"]

auth = tweepy.OAuthHandler(consumer_key=consumerKey,
                           consumer_secret=consumerSecret)

auth.set_access_token(accessKey, accessSecret)

api = tweepy.API(auth)
tweet_counts = api.trends_place(23424848)
results = tweet_counts[0]['trends']
frequencies = {}
for tweet in results:
    count = tweet['tweet_volume']
    if count == None:
        count = random.randint(10000, 30000)
    frequencies[tweet['name']] = count
trending_dict = frequencies
width, height = None, None
try:
    width, height = (
        (os.popen("xrandr | grep '*'").read()).split()[0]).split("x")
except:
    pass

configJSON = json.loads(open("config.json", "r").read())

if height and width:
    configJSON["resolution"]["width"] = int(width)
    configJSON["resolution"]["height"] = int(height)
    with open('config.json', 'w') as f:
        json.dump(configJSON, f, indent=4)

wc = WordCloud(
    background_color=configJSON["wordcloud"]["background"],
    width=int(configJSON["resolution"]["width"] -
              2 * configJSON["wordcloud"]["margin"]),
    height=int(configJSON["resolution"]["height"] -
               2 * configJSON["wordcloud"]["margin"])
).generate_from_frequencies(trending_dict)

wc.to_file('wc.png')

wordcloud = Image.open("wc.png")
wallpaper = Image.new('RGB', (configJSON["resolution"]["width"],
                              configJSON["resolution"]["height"]), configJSON["wordcloud"]["background"])
wallpaper.paste(
    wordcloud,
    (
        configJSON["wordcloud"]["margin"],
        configJSON["wordcloud"]["margin"]
    )
)
wallpaper.save("wallpaper.png")
