"""
Search module for the Twitter API
"""

# Author: Albin Bergvall
# Date: 2017-10-09
# Purpose: Class for gathering trending data from the twitter API. Uses a stream to gather
# tweets, and then saves it as dictionary to the file system. The dictionary can later be
# accessed and used to give titles a twitter based trending score.

import re
import time
import datetime
import pickle

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "911929395799035905-m0LQX9L0N3C47hCWG9tCDrIVWT6o9To"
access_token_secret = "gVdDlTqgqXx1JgjiaaGCLYmJV0vu3OkIKT7wMSAXniHyF"
consumer_key = "o5gC0O5nmnRhj7H1iRdq0LxBu"
consumer_secret = "Ef9M26RLwi6cZvsaESrFtuzffzgD3sNy7UnezOqzWbs5IDh2mY"

# Variables for tracked keywords in search,
# time until the stream stops and interval for saving to file.
tweets_data_path = 'trendingdata/twitter_data'
tracked_keywords = 'trailer,movie,film,dvd,cinema,episode'  # format is 'keyword1,keyword2,keyword3'
time_limit = 7200  # in seconds
interval = 600  # in seconds


class TwitterAPI:
    """
    Class responsible for saving twitter data to the file system
    via a stream, and also calculating a twitter trending score
    based on the data from the stream.
    """

    def __init__(self):
        self.all_words_new = {}
        self.all_words_old = {}

    @staticmethod
    def open_twitter_stream():
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To initiate a stream against the twitter API which listens for
        new tweets corresponding to a set of movie/series related keywords.
        The stream runs on a separate thread, and the duration of the stream as well
        as how often it will save the data can be set in the TwitterAPI.py file.
        :return:
        """
        output_stream = StdOutListener(time_limit, interval)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, output_stream)
        try:
            stream.filter(track=[tracked_keywords], languages=['en'], async=True)
        except:
            print("An error occurred. The twitter stream has been terminated.")

    def get_twitter_score(self, title):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To score a movie/series title based on the number of times each word
        in the title is mentioned in tweets. This method does not require a background model.
        :param title:
        :return twitter_score:
        """
        if not self.all_words_new:
            self.load_new_dict()
        title = title.lower()
        twitter_score = None
        words = title.split()
        for word in words:
            word = self.format_word(word)
            twitter_score = self.get_word_score(word, twitter_score, self.all_words_new)
        return twitter_score

    def get_twitter_score_freq_ratio(self, title):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To score a movie/series title based on the number of times each word
        in the title is mentioned in weets and how the frequency has changed compared to past.
        Requires a background model to compare with.
        :param title:
        :return:
        """
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
        score_ratio = self.chi_square(score_new, score_old)
        return score_ratio

    @staticmethod
    def chi_square(f_obs, f_exp):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: Static function used to determine a
        frequency ratio between new data and background model.
        f_obs is the new observed value, and f_exp is the old expected value.
        :param f_obs:
        :param f_exp:
        :return score_ratio:
        """
        return (f_obs - f_exp) ** 2 / f_exp

    @staticmethod
    def get_word_score(word, score, word_dict):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: This function is used to determine how many times
        a certain word has been mentioned.
        It will also compare the score to an already set score,
        and choose the one with fewer mentions.
        This is to give a score based on keyword mentions of the entire title.
        :param word:
        :param score:
        :param word_dict:
        :return:
        """
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
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: The purpose of this function is to load a saved dictionary from the file system.
        The file loaded will be from the day before.
        :return:
        """
        # yesterday = datetime.datetime.today() - timedelta(1)
        # path = tweets_data_path + yesterday.strftime('%Y%m%d') + ".bin"
        path = tweets_data_path + "_sample1.bin"  # This is the path to a temp file containing data for testing.
        with open(path, 'rb') as f:
            self.all_words_new = pickle.load(f)

    def load_old_dict(self):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: The purpose of this function is to load a saved dictionary from the file system.
        The file loaded will be from the a week ago and can be used as a background model.
        :return:
        """
        # earlier_date = datetime.datetime.today() - timedelta(7)
        # path = tweets_data_path + earlier_date.strftime('%Y%m%d') + ".bin"
        path = tweets_data_path + "_sample2.bin"
        with open(path, 'rb') as f:
            self.all_words_old = pickle.load(f)

    def print_dict(self):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To print the contents of a dictionary saved yesterday,
        descending from the key with highest value.
        :return:
        """
        if not self.all_words_new:
            self.load_new_dict()
        allwords_view = [(v, k) for k, v in self.all_words_new.items()]
        allwords_view.sort(reverse=True)
        for v, k in allwords_view:
            print(k, ": ", v)

    @staticmethod
    def format_word(word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To take a word as a parameter, format and return it
        so that it will be of same format as words stored from twitter stream.
        :param word:
        :return:
        """
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word


class StdOutListener(StreamListener):
    """
    Listener class used for twitter stream. Function on_status is called
    each time a tweet corresponding to a set of keywords is picked up by stream.
    Also contains functions for formatting words, saving them to a dictionary and
    lastly saving the dictionary to the file system.
    """

    def __init__(self, limit, interval_time):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: Constructor for the stream class.
        Takes time limit for the stream as parameter,
        as well as an interval for how often it should be saved to file.
        :param limit:
        :param interval_time:
        """
        self.start_time = time.time()
        self.limit = limit
        self.interval_time = interval_time
        self.interval = self.interval_time
        self.all_words = {}
        super(StdOutListener, self).__init__()

    def on_status(self, status):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: This function is called each time a tweet is picked up by the filter.
        It checks if time limits has been exceeded for saving to file,
        and also takes the tweet text, splits it, and then calls other functions for
        formatting and saving the words to a dictionary.
        :param status:
        :return:
        """
        if(time.time() - self.start_time) > self.interval_time:
            self.store_dict()
            print("Stored at interval time:", self.interval_time, "s")
            self.interval_time += self.interval
        if(time.time() - self.start_time) < self.limit:
            words = status.text.split()
            for word in words:
                word = self.format_word(word)
                if word is not None:
                    self.update_count(word)
            return True
        else:
            self.store_dict()
            return False

    @staticmethod
    def format_word(word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To take a word as a parameter, format it and return the word
        if there is anything left after doing a regex check over the characters of the word.
        Otherwise, return None.
        :param word:
        :return word:
        """
        word = word.lower()
        word = word.strip(" ")
        regex = re.compile('[^a-z0-9]')
        word = regex.sub('', word)
        if word == "" or word.startswith("httpstco"):
            return None
        return word

    def on_error(self, status):
        """
        Purpose: Function which is called if there was an error with the stream.
        Saves the dictionary and closes stream.
        :param status:
        :return:
        """
        self.store_dict()
        print(status)

    def update_count(self, word):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To save a word to the dictionary if it hasn't been mentioned yet,
        otherwise increase the count of an already mentioned word.
        :param word:
        :return:
        """
        if word in self.all_words:
            val = self.all_words.get(word)
            val += 1
            self.all_words[word] = val
        else:
            self.all_words[word] = 1

    def store_dict(self):
        """
        Author: Albin Bergvall, Karl Lundvall
        Purpose: To save a dictionary to a file in the trendingdata folder.
        The name of the file will include the date of when it was saved.
        This way, we will know from which day data was stored.
        :return:
        """
        path = tweets_data_path + datetime.datetime.today().strftime('%Y%m%d') + ".bin"
        with open(path, 'wb') as f:
            pickle.dump(self.all_words, f, pickle.HIGHEST_PROTOCOL)
            f.close()
        print("Dictionary saved to file! Path:", path)


# For stream testing purposes
if __name__ == "__main__":
    tw = TwitterAPI()
    tw.open_twitter_stream()
