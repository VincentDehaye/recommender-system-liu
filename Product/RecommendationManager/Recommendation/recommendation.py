"""
Recommendation Class.
"""
import numpy as np
from Product.RecommendationManager import generate_model as generate_model
from Product.Database.DBConn import session, TrendingScore
from Product.RecommendationManager import gets_from_database as gets_from_database
from Product.RecommendationManager.Recommendation.recommendation_list import RecommendationList


# At this point we assume that there is a file named new_model.sav
class Recommendation(object):
    """
    Author: Sebastian Maghsoudi / Alexander Dahl
    Date: 2017-11-01
    Last update: 2017-11-09 by Alexander Dahl
    Purpose:
    creates a recommendation class
    """
    def __init__(self, user_id, size):
        """
        Author: Sebastian Maghsoudi / Alexander Dahl
        Date: 2017-11-01
        Last update: 2017-11-09 by Alexander Dahl
        Purpose: constructor for the recommendation class

        :param user_id: a user_id
        :param size: how many movies should be recommended

        model is a lightfm model that has been saved in a folder above
        trending_content_meta is the normalized scores for trending_scores
        the number of fetched trending_content_meta is limited by the lim variable

        """
        # TODO should the class assume that there is a model named 'new_model.sav'?
        self.model = generate_model.load_model('../new_model.sav')
        self.user_id = user_id
        # right now lim is hard coded to number of movies to be recommended times 3
        # TODO create some logic for how big the limit should be
        self.lim = size*3
        self.size = size
        # TODO move trending_content_meta to DataBaseManager
        self.trending_content_meta = session.query(TrendingScore.movie_id, TrendingScore.normalized_score).order_by(TrendingScore.normalized_score.desc()).limit(self.lim).all()

    @staticmethod
    def normalize_user_scores(scores):
        """
        Author: Gustaf Norberg / Alexander Dahl
        Date: 2017-10-30
        Last update: 2017-10-30
        Purpose: normalizes the scores to be between 0 and 1.

        :return: list of scores
        """
        min_score = np.amin(scores)
        max_score = np.amax(scores)

        for i in range(0, len(scores)):
            scores[i] = (scores[i] - min_score)/(max_score-min_score)
        return scores

    def generate_recommendation_list(self):
        """
        Author: Sebastian Maghsoudi / Alexander Dahl
        Date: 2017-11-01
        Last update: 2017-11-09
        Purpose: Generates a recommendation list of size length for a given user.

        :return: a dictionary with user_id and a recommendation_list for that user
        example:
        {'user_id': 55, 'recommendation_list' : [{'title': 'It', 'score': 1.586134233975164, 'id': 24}]}
        """
        trending_id = [id[0] for id in self.trending_content_meta]
        recommendation_list_score = self.model.predict(self.user_id, np.array(trending_id))
        norm_recommendation_list_score = self.normalize_user_scores(recommendation_list_score).tolist()
        trending_score = [score[1] for score in self.trending_content_meta]
        # trending_weight is 1 at the moment
        trending_weight=1
        # Here is the formula that can be altered at some point
        final_recommendation_list_score = [rec+trending_weight*trend for rec, trend in zip(norm_recommendation_list_score,trending_score)]
        # gets the movie titles for the movie ids
        movie_titles = [gets_from_database.get_movie_title(id[0]) for id in self.trending_content_meta]
        # combines the movie_ids and movie_titles with the recommendation scores
        full_recommendation_list = list(map(list,zip(trending_id,movie_titles,final_recommendation_list_score)))
        # sorts the list on scores (index 2)
        sorted_recommendation_list = sorted(full_recommendation_list,
                                            key=lambda x: x[2],
                                            reverse=True)

        sorted_complete_recommendation_list = []
        for item in sorted_recommendation_list[:self.size]:
            sorted_complete_recommendation_list.append({'id': item[0],
                                                        'title': item[1],
                                                        'score': item[2]})
        #print(sorted_complete_recommendation_list)
        return RecommendationList(self.user_id, sorted_complete_recommendation_list)

print(Recommendation(55, 10).generate_recommendation_list().__dict__)
