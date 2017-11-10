from Product.Database.Retrieve.Retrieve import Retrieve
from Product.Database.DBConn import TrendingScore

'''
Author: John Andree Lidquist, Marten Bolin
Date: 9/11/2017
Last update: 10/11/2017
Purpose: Supposed to Retrieve data from trending table in database
'''

class RetrieveTrending(Retrieve):

    def retrieve_trend_score(self, movie_id=None):
        if movie_id:
            trend=self.session.query(TrendingScore).filter_by(movie_id=movie_id).first()
        else:
            trend=self.session.query(TrendingScore).all()
        self.session.close()
        return trend

