from Product.Database.Update.Update import Update
from Product.Database.DBConn import TrendingScore
'''
Author: John Andree Lidquist, Marten Bolin
Date: 9/11/2017
Last update: 10/11/2017
Purpose: Supposed to update data in trending table in database
'''


class UpdateTrending(Update):

    def update_trend_score(self, movie_id, total_score=None, youtube_score=None, twitter_score=None):
        to_update = self.session.query(TrendingScore).filter_by(movie_id=movie_id)
        if total_score:
            to_update.total_score=total_score
        if youtube_score:
            to_update.youtube_score=youtube_score
        if twitter_score:
            to_update.twitter_score=twitter_score
        self.session.commit()
        self.session.close()