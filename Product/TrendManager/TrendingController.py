"""
Author: Albin Bergvall, Martin Bergvall
Date: 2017-09-28
Last update: 2017-10-03
Purpose: TrendingController runs the API's and calculates a total trending score
"""


from Product.TrendManager.YoutubeAPI import YoutubeAPI
from Product.TrendManager.TwitterAPI import TwitterAPI
from googleapiclient.errors import HttpError


class TrendingController:
    """""
    Author: Albin Bergvall, Martin Lundberg
    Date: 2017-09-28
    Last update: 2017-10-03
    Purpose: Class responsible for fetching the trending score from the API sources.
    """

    @staticmethod
    def get_trending_content(keyword):
        """
        Author: Albin Bergvall, Martin Lundberg
        Date:
        Last update:
        Purpose: Takes the movie title (keyword) as a parameter and fetches score
        from the API sources and returns a numeric result.
        :param keyword: keyword, e.g. movie title
        :return: total_score, youtube_score, twitter_score
        """
        total_score = 0
        try:
            youtube_score = YoutubeAPI().get_youtube_score(keyword)
        except HttpError:
            print("The daily quota of youtube requests have been reached.")
        twitter_score = TwitterAPI().get_twitter_score(keyword) * 100
        total_score += youtube_score + twitter_score
        return total_score, youtube_score, twitter_score
