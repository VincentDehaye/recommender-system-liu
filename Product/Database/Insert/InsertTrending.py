from Product.Database.Insert import Insert
from Product.Database.DBConn import TrendingScore


class InsertTrending(Insert):
    def add_trend_score(self, movie_id, total_score, youtube_score, twitter_score):
        movie = TrendingScore(movie_id=movie_id, total_score=total_score, youtube_score=youtube_score,
                              twitter_score=twitter_score)
        self.session.add(movie)
        self.session.commit()
