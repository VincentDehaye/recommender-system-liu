# Author: Albin Bergvall
# Date: 2017-10-09
# Purpose: Class for gathering trending data from the twitter API. Uses a stream to gather
# tweets, and then saves it as a background model to be compared with new data.
# This way, we can see if certain keywords (movie titles) increase or decrease
# in frequency.
# Class was built using following guide: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

# Import the necessary methods from tweepy library
import threading

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import re
import time
import pickle

# Variables that contains the user credentials to access Twitter API
access_token = "911929395799035905-m0LQX9L0N3C47hCWG9tCDrIVWT6o9To"
access_token_secret = "gVdDlTqgqXx1JgjiaaGCLYmJV0vu3OkIKT7wMSAXniHyF"
consumer_key = "o5gC0O5nmnRhj7H1iRdq0LxBu"
consumer_secret = "Ef9M26RLwi6cZvsaESrFtuzffzgD3sNy7UnezOqzWbs5IDh2mY"
tweets_data_path = 'trendingdata/twitter_data.txt'


class TwitterAPI:

    def word_in_text(self, word, text):
        word = word.lower()
        text0 = str(text)
        text0 = text0.lower()
        match = re.search(word, text0)
        if match:
            return True
        return False



allwords = {}

def format_word(word):
    word = word.lower()
    word = word.strip(" ")
    regex = re.compile('[^a-z]')
    word = regex.sub('', word)
    if word == "":
        return None
    return word


def update_count(word):
    if word in allwords:
        val = allwords.get(word)
        val += 1
        allwords[word] = val
    else:
        allwords[word] = 1


def print_dict():
    allwords_view = [(v, k) for k ,v in allwords.items()]
    allwords_view.sort(reverse=True)
    for v, k in allwords_view:
        print(k, ": ", v)


def store_dict():
    with open(tweets_data_path, 'wb') as f:
        pickle.dump(allwords, f, pickle.HIGHEST_PROTOCOL)
    print("Dictionary saved to file! Path:", tweets_data_path)


def load_dict():
    with open(tweets_data_path, 'rb') as f:
        return pickle.load(f)

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
        #all_data = json.loads(data)
        #lang = all_data['lang']
        #if lang == 'en':
        #tweet = all_data['text']
        words = status.text.split()
        for word in words:
            word = format_word(word)
            if word is not None:
                update_count(word)
        return True

    def on_error(self, status):
        print(status)


# For testing purposes
if __name__ == '__main__':

    # This handles Twitter authetification and the connection to Twitter Streaming API
    outputStream = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, outputStream)

    # This line filter Twitter Streams to capture data by the keywords specified
    '''
    try:
        stream.filter(track=['trailer', 'movie', 'show'], languages=['en'], async=True)
    except:
        print("Stream stopped")
    time.sleep(60)
    store_dict()
    '''
    allwords = load_dict()
    allwords_view = [(v, k) for k, v in allwords.items()]
    allwords_view.sort(reverse=True)
    for v, k in allwords_view:
        print(k, ": ", v)