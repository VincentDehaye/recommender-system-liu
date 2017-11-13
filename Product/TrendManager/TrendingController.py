# Author: Martin Lundberg, Albin Bergvall
# Date: 2017-09-28
# Updated: 2017-10-03
# Purpose: Controller class for the trending module. Gets data, calculates a score
# and sends it to the database API.


from Product.TrendManager.YoutubeAPI import YoutubeAPI
from Product.TrendManager.TwitterAPI import TwitterAPI


class TrendingController:

    def __init__(self):
        self.youtubeapi = YoutubeAPI()
        self.twitterapi = TwitterAPI()
        # SendToDatabase(scoredMovie)

    def get_trending_content(self, searchterm):
        return self.total_score_calc(searchterm)

    def total_score_calc(self, keyword):
        totalscore = 0
        youtubescore = self.youtubeapi.get_youtube_score(keyword)
        twitterscore = self.twitterapi.get_twitter_score(keyword)

        # add more scoreres as needed
        totalscore += youtubescore + twitterscore
        return totalscore, youtubescore, twitterscore


if __name__ == "__main__":
    #keyword = input()
    tc = TrendingController()
    #print(tc.get_trending_content(keyword).score)
    #tc.get_trending_content(keyword)