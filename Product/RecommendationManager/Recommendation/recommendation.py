"""
Recommendation Class.
"""
import numpy as np
import os
from Product.RecommendationManager import generate_model as generate_model
from Product.RecommendationManager import gets_from_database as gets_from_database
from Product.RecommendationManager.Recommendation.recommendation_list import RecommendationList
from Product.Database.DatabaseManager.Retrieve.RetrieveTrending import RetrieveTrending


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
        Last update: 2017-11-13 by Alexander Dahl
        Purpose: constructor for the recommendation class

        :param user_id: a user_id
        :param size: how many movies should be recommended

        model is a lightfm model that has been saved in a folder above
        trending_content_meta is the normalized scores for trending_scores
        the number of fetched trending_content_meta is limited by the lim variable

        """
        # TODO should the class assume that there is a model named 'new_model.sav'?
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.model = generate_model.load_model(path + '/new_model.sav')
        self.user_id = user_id
        # right now lim is hard coded to number of movies to be recommended times 3
        # TODO create some logic for how big the limit should be
        self.lim = size*3
        self.size = size
        # this instantiates RetrieveTrending() class in the database manager and
        # gets limit number of TrendingScore classes.
        self.trending_content_meta = RetrieveTrending().\
            retrieve_trend_score(number_of_titles=self.lim)

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
        Last update: 2017-11-13
        Purpose: Generates a recommendation list of size length for a given user.

        :return: a dictionary with user_id and a recommendation_list for that user
        example:
        {'user_id': 55, 'recommendation_list' :
        [{'title': 'It', 'score': 1.586134233975164, 'id': 24}]}
        """
        trending_id = [id.movie_id for id in self.trending_content_meta]
        print(np.array(trending_id))
        # TODO this only makes user preference scores on items that are part of the
        # TODO 30 limit trending list
        # TODO should it really be like that?
        rec_list_score = self.model.predict(self.user_id, np.array(trending_id))
        norm_rec_list_score = self.normalize_user_scores(rec_list_score).tolist()
        trending_score = [score.total_score for score in self.trending_content_meta]
        # normalize trending score
        norm_trending_score = self.normalize_user_scores(trending_score)
        # trending_weight is 1 at the moment
        trending_weight = 1
        # Here is the formula that can be altered at some point
        final_rec_list_score = [rec+trending_weight*trend for rec, trend
                                in zip(norm_rec_list_score, norm_trending_score)]
        # gets the movie titles for the movie ids
        movie_titles = [gets_from_database.get_movie_title(id.movie_id) for id
                        in self.trending_content_meta]
        # combines the movie_ids and movie_titles with the recommendation scores
        full_rec_list = list(map(list, zip(trending_id, movie_titles, final_rec_list_score)))
        # sorts the list on scores (index 2)
        sorted_rec_list = sorted(full_rec_list,
                                 key=lambda x: x[2],
                                 reverse=True)

        sorted_complete_rec_list = []
        for item in sorted_rec_list[:self.size]:
            sorted_complete_rec_list.append({'id': item[0],
                                             'title': item[1],
                                             'score': item[2]})
        # print(sorted_complete_rec_list)
        return RecommendationList(self.user_id, sorted_complete_rec_list)

# print(Recommendation(55, 10).generate_recommendation_list().__dict__)
