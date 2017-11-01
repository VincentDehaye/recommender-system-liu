from Product.RecommendationManager import generateModel as generate_model
from Product.Database.DBConn import session, TrendingScore

#At this point we assume that there is a file namned new_model.sav
class Recommendation(object):
    def __init__(self):
        self.model = generate_model.load_model('../new_model.sav')

    def set_trend(self, lim):
        self.Trending_Content_Meta = session.query(TrendingScore.movie_id, TrendingScore.normalized_score).order_by(TrendingScore.normalized_score.desc()).limit(lim).all()


rec = Recommendation()
rec.set_trend(20)
print(rec.Trending_Content_Meta)