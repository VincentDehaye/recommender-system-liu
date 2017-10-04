# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.


import YoutubeAPI
from ScoredMovie import ScoredMovie
from oauth2client.tools import argparser
import sys  # To be able to run from comandpropt

class TrendingController:

    #def __init__(self, searchterm):
        # SendToDatabase(scoredMovie)

    def get_trending_content(self, searchterm):
        scoredmovie = ScoredMovie(1,
                                  self.total_score_calc(searchterm))  # temp id, use id from database/imdb id?
        return scoredmovie

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
            totalviews += int(video["statistics"]["viewCount"])
        return totalviews

    # def SendToDatabase(self, scoredMovie):


"""
Argparser to send title as argument when running script, --c "title"
"""
# argparser.add_argument("--c", help="Content title", default="")
# argparser.parse_args()
# if __name__ == "__main__":
   # searchterm = str(sys.argv[2])
   # trendingcontroller = TrendingController()
   # scoredmovie = TrendingController.get_trending_content(trendingcontroller, searchterm)
   # print(scoredmovie.score)

"""
Ask user for input after script is run
"""
searchterm = input("Enter content title: ")
trendingcontroller = TrendingController()
scoredmovie = TrendingController.get_trending_content(trendingcontroller, searchterm)
print(scoredmovie.score)
