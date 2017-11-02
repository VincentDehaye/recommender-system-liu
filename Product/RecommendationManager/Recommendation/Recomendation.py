from Product.RecommendationManager import generateModel as generate_model
from Product.Database.DBConn import session, TrendingScore, Rating
import numpy as np

#At this point we assume that there is a file namned new_model.sav
class Recommendation(object):
    def __init__(self, user_id, lim, size):
        self.model = generate_model.load_model('../new_model.sav')
        self.user_id = user_id
        self.lim = lim
        self.size = size

    def set_trend(self):
        self.Trending_Content_Meta = session.query(TrendingScore.movie_id, TrendingScore.normalized_score).order_by(TrendingScore.normalized_score.desc()).limit(self.lim).all()

    @staticmethod
    def normalize_user_scores(scores):
        min_score = np.amin(scores)
        max_score = np.amax(scores)

        for i in range(0, len(scores)):
            scores[i] = (scores[i] - min_score)/(max_score-min_score)
        return scores

    def generate_recommendation_list(self):
        trending_id = [id[0] for id in self.Trending_Content_Meta]
        recommendation_list_score = self.model.predict(self.user_id, np.array(trending_id))
        norm_recommendation_list_score = self.normalize_user_scores(recommendation_list_score).tolist()
        trending_score = [score[1] for score in self.Trending_Content_Meta]
        #Here is the formula that can be altered at some point
        final_recommendation_list_score = [rec+1.5*trend for rec, trend in zip(norm_recommendation_list_score,trending_score)]
        full_recommendation_list = list(map(list,zip(trending_id,final_recommendation_list_score)))
        sorted_full_recommendation_list = sorted(full_recommendation_list,key=lambda x: x[1], reverse=True)
        print(sorted_full_recommendation_list[:self.size])

rec = Recommendation(5, 30, 10)
rec.set_trend()
rec.generate_recommendation_list()