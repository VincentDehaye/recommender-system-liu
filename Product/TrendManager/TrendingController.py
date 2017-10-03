# Author: Martin Lundberg,
# Date: 2017-09-28
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.

# from .YoutubeAPI import YoutubeAPI
from .ScoredMovie import ScoredMovie

# This is just a suggestion of how the TrendingController could look like.
# We don't know what the data from the youtubeApi will look like yet.


class TrendingController:
    scoredMovie = ScoredMovie()

    def __init__(self):
        # self.youtubeData = YoutubeAPI.getData("Keyword")
        # scoredMovie.id = self.youtubeData[id]
        # scoredMovie.score = YoutubeScoreCalc(self.youtubeData[views], other...)
        # SendToDatabase(scoredMovie)
        print ("placeholder")

    # def YoutubeScoreCalc(self, views, other...):

    # def SendToDatabase(self, scoredMovie):