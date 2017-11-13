# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.
from Product.TrendManager.YoutubeAPI import YoutubeAPI
from Product.TrendManager.TwitterAPI import TwitterAPI


class TrendingController:
    """""
    Class responsible for fetching the trending score from the api sources.
    """

    def get_trending_content(self, search_term):
        """
        Author: Albin Bergvall, Martin Lundberg
        Takes a movie title (search_term) and make the search in the
        api sources and returns a numeric result for each api source.
        :param search_term:
        :return:
        """
        return self.total_score_calc(search_term)

    def total_score_calc(self, keyword):
        """
        Author: Albin Bergvall, Martin Lundberg
        Takes the movie title (keyword) as a parameter and fetches score from the api sources
        and returns a numeric result.
        :param keyword:
        :return: total_score, youtube_score, twitter_score
        """
        total_score = 0
        youtube_score = YoutubeAPI().get_youtube_score(keyword)
        twitter_score = TwitterAPI().get_twitter_score(keyword)
        total_score += youtube_score + twitter_score
        return total_score, youtube_score, twitter_score