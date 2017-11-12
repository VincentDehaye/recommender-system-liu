# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.


from Product.TrendManager.YoutubeAPI import YoutubeAPI
from Product.TrendManager.ScoredMovie import ScoredMovie


class TrendingController:

    def __init__(self):
        self.youtubeapi = YoutubeAPI()
        # SendToDatabase(scoredMovie)

    def get_trending_content(self, searchterm):
        #scoredmovie = ScoredMovie(1, self.total_score_calc(searchterm))  # temp id, use id from database/imdb id?
        return self.total_score_calc(searchterm)

    def total_score_calc(self, keyword):
        totalscore = 0
        youtubescore = self.youtubeapi.get_youtube_score(keyword)
        twitterscore = 0
        # add more scoreres as needed
        totalscore += youtubescore
        return totalscore, youtubescore, twitterscore

    # def SendToDatabase(self, scoredMovie):


if __name__ == "__main__":
    #keyword = input()
    tc = TrendingController()
    #print(tc.get_trending_content(keyword).score)
    #tc.get_trending_content(keyword)