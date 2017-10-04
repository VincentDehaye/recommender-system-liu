# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.

from Product.TrendManager import YoutubeAPI
from Product.TrendManager.ScoredMovie import ScoredMovie


class TrendingController:
    # scoredMovie = ScoredMovie()

    def __init__(self):
        searchterm = "frozen"  # Quick test of class, change searchterm for different searches
        scoredmovie = ScoredMovie(1,
                                  self.total_score_calc(searchterm))  # temp id, use id from database/imdb id?
        print("Search term: " + searchterm + ", Score: " + scoredmovie.score)
        # scoredMovie.score = YoutubeScoreCalc(self.youtubeData[views], other...)
        # SendToDatabase(scoredMovie)

    def total_score_calc(self, keyword):
        totalscore = 0
        youtubescore = self.youtube_score_calc(keyword)
        # add more scoreres as needed
        totalscore += youtubescore
        return totalscore

    def youtube_score_calc(self, keyword):
        youtubedata = YoutubeAPI.get_youtube_count(keyword)
        totalviews = 0
        for video in youtubedata.get("items", []):
            totalviews += video["statistics"]["viewCount"]
        return totalviews

        # def SendToDatabase(self, scoredMovie):
