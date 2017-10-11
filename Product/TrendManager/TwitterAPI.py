# Author: Albin Bergvall
# Date: 2017-10-09
# Purpose: Class for gathering trending data from the twitter API. Uses a stream to gather
# tweets, and then saves it as a background model to be compared with new data.
# This way, we can see if certain keywords (movie titles) increase or decrease
# in frequency.
# Class was built using following guide: http://adilmoujahid.com/posts/2014/07/twitter-analytics/

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import re

# Variables that contains the user credentials to access Twitter API
access_token = "911929395799035905-m0LQX9L0N3C47hCWG9tCDrIVWT6o9To"
access_token_secret = "gVdDlTqgqXx1JgjiaaGCLYmJV0vu3OkIKT7wMSAXniHyF"
consumer_key = "o5gC0O5nmnRhj7H1iRdq0LxBu"
consumer_secret = "Ef9M26RLwi6cZvsaESrFtuzffzgD3sNy7UnezOqzWbs5IDh2mY"
tweets_data_path = 'trendingdata/twitter_data.txt'


class TwitterAPI:
    # def __init__(self):
    #    auth = OAuthHandler(consumer_key, consumer_secret)
    #    auth.set_access_token(access_token, access_token_secret)

    def process_data(self):
        tweets_data = []
        tweets_file = open(tweets_data_path, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_data.append(tweet)
            except:
                continue

        tweets = pd.DataFrame()
        tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
        tweets['frozen'] = tweets['text'].apply(lambda tweet: self.word_in_text('frozen', tweet))
        tweets['wonder woman'] = tweets['text'].apply(lambda tweet: self.word_in_text('wonder woman', tweet))
        tweets['titanic'] = tweets['text'].apply(lambda tweet: self.word_in_text('titanic', tweet))
        tweets['relevant'] = tweets['text'].apply(lambda tweet: self.word_in_text('movie', tweet) or
                                                                self.word_in_text('trailer', tweet) or
                                                                self.word_in_text('scene', tweet) or
                                                                self.word_in_text('cinema', tweet) or
                                                                self.word_in_text('watch', tweet) or
                                                                self.word_in_text('picture', tweet) or
                                                                self.word_in_text('tv', tweet) or
                                                                self.word_in_text('show', tweet) or
                                                                self.word_in_text('award', tweet) or
                                                                self.word_in_text('dvd', tweet) or
                                                                self.word_in_text('stream', tweet))
        return tweets

    def word_in_text(self, word, text):
        word = word.lower()
        text0 = str(text)
        text0 = text0.lower()
        match = re.search(word, text0)
        if match:
            return True
        return False

    def print_counts(self):
        tweets = self.process_data()
        print(tweets[tweets['relevant'] == True]['frozen'].value_counts()[True])
        print(tweets[tweets['relevant'] == True]['wonder woman'].value_counts()[True])
        print(tweets[tweets['relevant'] == True]['titanic'].value_counts()[True])


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
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
    stream.filter(track=['frozen', 'wonder woman', 'titanic'])
