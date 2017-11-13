# Author: Albin Bergvall
# Date: 2017-10-09
# Purpose: Class for gathering trending data from the twitter API. Uses a stream to gather
# tweets, and then saves it as a background model to be compared with new data.
# This way, we can see if certain keywords (movie titles) increase or decrease
# in frequency.

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re
import time
import datetime
from datetime import timedelta
import pickle


# Variables that contains the user credentials to access Twitter API
access_token = "911929395799035905-m0LQX9L0N3C47hCWG9tCDrIVWT6o9To"
access_token_secret = "gVdDlTqgqXx1JgjiaaGCLYmJV0vu3OkIKT7wMSAXniHyF"
consumer_key = "o5gC0O5nmnRhj7H1iRdq0LxBu"
consumer_secret = "Ef9M26RLwi6cZvsaESrFtuzffzgD3sNy7UnezOqzWbs5IDh2mY"
tweets_data_path = 'trendingdata/twitter_data'

# Variables for tracked keywords in search, time until the stream stops and interval for saving to file
tracked_keywords = 'trailer,movie,film,dvd,cinema,episode'  # format is 'keyword1,keyword2,keyword3' etc.
time_limit = 7200  # in seconds
interval = 600  # in seconds


class TwitterAPI:

    def __init__(self):
        self.all_words_new = {}
        self.all_words_old = {}

    def open_twitter_stream(self):
        output_stream = StdOutListener(time_limit, interval)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, output_stream)
        try:
            stream.filter(track=[tracked_keywords], languages=['en'], async=True)
        except:
            print("An error occurred. The twitter stream has been terminated.")

    def get_twitter_score(self, title):
        if not self.all_words_new:
            self.load_new_dict()
        if not self.all_words_old:
            self.load_old_dict()
        title = title.lower()
        score_new = None
        score_old = None
        words = title.split()
        for word in words:
            word = self.format_word(word)
            score_new = self.get_word_score(word, score_new, self.all_words_new)
            score_old = self.get_word_score(word, score_old, self.all_words_old)
        if score_new < 10:
            score_new = 10
        if score_old < 10:
            score_old = 10
        print("Old:", score_old, "New:", score_new)
        score_ratio = self.chi_square(score_new, score_old)
        return score_ratio

    def chi_square(self, f_obs, f_exp):
        return (f_obs - f_exp) ** 2 / f_exp

    def get_word_score(self, word, score, word_dict):
        if word in word_dict:
            curr_score = word_dict.get(word)
            if score is None:
                score = curr_score
            elif curr_score < score:
                score = curr_score
        else:
            score = 0
        return score

    def load_new_dict(self):
        # yesterday = datetime.datetime.today() - timedelta(1)
        # path = tweets_data_path + yesterday.strftime('%Y%m%d') + ".bin"
        path = tweets_data_path + "_sample1.bin"
        with open(path, 'rb') as f:
            self.all_words_new = pickle.load(f)

    def load_old_dict(self):
        # earlier_date = datetime.datetime.today() - timedelta(7)
        # path = tweets_data_path + earlier_date.strftime('%Y%m%d') + ".bin"
        path = tweets_data_path + "_sample2.bin"
        with open(path, 'rb') as f:
            self.all_words_old = pickle.load(f)

    def print_dict(self):
        if not self.all_words_new:
            self.load_new_dict()
        allwords_view = [(v, k) for k, v in self.all_words_new.items()]
        allwords_view.sort(reverse=True)
        for v, k in allwords_view:
            print(k, ": ", v)


    def format_word(self, word):
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word


def word_in_text(word, text):
    word = word.lower()
    text0 = str(text)
    text0 = text0.lower()
    match = re.search(word, text0)
    if match:
        return True
    return False


# This is a basic listener that runs
class StdOutListener(StreamListener):

    def __init__(self, limit, interval_time):
        self.start_time = time.time()
        self.limit = limit
        self.interval_time = interval_time
        self.interval = self.interval_time
        self.all_words = {}
        super(StdOutListener, self).__init__()

    def on_status(self, status):
        if(time.time() - self.start_time) > self.interval_time:
            self.store_dict()
            print("Stored at interval time:", self.interval_time, "s")
            self.interval_time += self.interval
        if(time.time() - self.start_time) < self.limit:
            word = status.text
            words = status.text.split()
            for word in words:
                word = self.format_word(word)
                if word is not None:
                    self.update_count(word)
                return True
        else:
            self.store_dict()
            return False

    def format_word(self, word):
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word

    def on_error(self, status):
        self.store_dict()
        print(status)

    def update_count(self, word):
        if word in self.all_words:
            val = self.all_words.get(word)
            val += 1
            self.all_words[word] = val
        else:
            self.all_words[word] = 1

    def store_dict(self):
        path = tweets_data_path + datetime.datetime.today().strftime('%Y%m%d') + ".bin"
        with open(path, 'wb') as f:
            pickle.dump(self.all_words, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        print("Dictionary saved to file! Path:", path)


# For testing purposes
if __name__ == '__main__':
    twAPI = TwitterAPI()
    #twAPI.open_twitter_stream()
    # twAPI.print_dict()
    print(twAPI.get_twitter_score("thor"))

