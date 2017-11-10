from Product.Database.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import TrendingScore
from sqlalchemy import desc
'''
Author: John Andree Lidquist, Marten Bolin
Date: 9/11/2017
Last update: 10/11/2017
Purpose: Supposed to Retrieve data from trending table in database
'''

class RetrieveTrending(Retrieve):

    def retrieve_trend_score(self, movie_id=None, number_of_titles=None):
        if movie_id:
            trend=self.session.query(TrendingScore).filter_by(movie_id=movie_id).first()
        elif number_of_titles:
            trend=self.session.query(TrendingScore).order_by(desc(TrendingScore.total_score)).limit(number_of_titles)
        else:
            trend=self.session.query(TrendingScore).all()
        self.session.close()
        return trend

    def get_trending_twitter(self, numOfTitles):
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.twitter_score)).limit(numOfTitles)
        return query

    def get_trending_youtube(self, numOfTitles):
        query = self.session.query(TrendingScore).order_by(desc(TrendingScore.youtube_score)).limit(numOfTitles)
        return query