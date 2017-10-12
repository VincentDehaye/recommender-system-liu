# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.


from YoutubeAPI import YoutubeAPI
from ScoredMovie import ScoredMovie


class TrendingController:

    def __init__(self):
        self.youtubeapi = YoutubeAPI()
        # SendToDatabase(scoredMovie)

    def get_trending_content(self, searchterm):
        scoredmovie = ScoredMovie(1,
                                  self.total_score_calc(searchterm))  # temp id, use id from database/imdb id?
        return scoredmovie

    def total_score_calc(self, keyword):
        totalscore = 0
        youtubescore = self.youtubeapi.get_youtube_count(keyword)
        # add more scoreres as needed
        print(youtubescore)
        totalscore += youtubescore
        return totalscore

    # def SendToDatabase(self, scoredMovie):

tc = TrendingController()
tc.get_trending_content("It")