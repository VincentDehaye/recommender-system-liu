from Product.RecommendationManager import generate_model as generate_model
from Product.Database.DBConn import session, TrendingScore, Rating
from Product.RecommendationManager import gets_from_database as gets_from_database

import numpy as np
from Product.RecommendationManager.Recommendation.recommendation_list import RecommendationList

#At this point we assume that there is a file namned new_model.sav
class Recommendation(object):
    """
    creates a recommendation class
    """
    def __init__(self, user_id, lim, size):
        """
        constructor for the recommendation class
        :param user_id: a user_id
        :param lim: limit on how many trending scores should be fetched from database
        :param size: how many movies should be recommended

        model is a lightfm model that has been saved in a folder above
        trending_content_meta is the normalized scores for trending_scores
        the number of fetched trending_content_meta is limited by the lim variable

        """
        self.model = generate_model.load_model('../new_model.sav')
        self.user_id = user_id
        self.lim = lim
        self.size = size
        # TODO move trending_content_meta to DataBaseManager
        self.trending_content_meta = session.query(TrendingScore.movie_id, TrendingScore.normalized_score).order_by(TrendingScore.normalized_score.desc()).limit(lim).all()

    @staticmethod
    def normalize_user_scores(scores):
        min_score = np.amin(scores)
        max_score = np.amax(scores)

        for i in range(0, len(scores)):
            scores[i] = (scores[i] - min_score)/(max_score-min_score)
        return scores

    def generate_recommendation_list(self):
        trending_id = [id[0] for id in self.trending_content_meta]
        recommendation_list_score = self.model.predict(self.user_id, np.array(trending_id))
        norm_recommendation_list_score = self.normalize_user_scores(recommendation_list_score).tolist()
        trending_score = [score[1] for score in self.trending_content_meta]
        #Here is the formula that can be altered at some point
        final_recommendation_list_score = [rec+1*trend for rec, trend in zip(norm_recommendation_list_score,trending_score)]
        movie_titles = [gets_from_database.get_movie_title(id[0]) for id in self.trending_content_meta]
        full_recommendation_list = list(map(list,zip(trending_id,movie_titles,final_recommendation_list_score)))
        # sorts the list
        sorted_recommendation_list = sorted(full_recommendation_list, key=lambda x: x[2], reverse=True)
        innerdict={}
        sorted_complete_recommendation_list=[]
        for item in sorted_recommendation_list[:self.size]:
            # creates an inner dictionary to get the correct output structure
            innerdict['id', 'title', 'score'] = item[0], item[1], item[2]
            #print(innerdict)
            # has to do a copy otherwise it references the original dictionary
            # we only want the last generated dict and not all of it.
            sorted_complete_recommendation_list.append(innerdict.copy())
        #print(sorted_complete_recommendation_list)
        return RecommendationList(self.user_id, sorted_complete_recommendation_list)

print(Recommendation(55, 30, 10).generate_recommendation_list().__dict__)
