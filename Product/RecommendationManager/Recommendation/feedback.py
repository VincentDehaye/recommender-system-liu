import os
from Product.Database.DatabaseManager.Insert.InsertFeedback import InsertFeedback
from Product.RecommendationManager.model import generate_model as generate_model
from Product.Database.DatabaseManager.Retrieve.RetrieveMovie import RetrieveMovie
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser

import scipy.sparse as sp

class Feedback(object):
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-17
    Last update:
    Purpose: Make Insert of sent Feedback
    """
    @staticmethod
    def insert_feedback(user_id, movie_id, watched=None, rating=None):
            """
            Author: Alexander Dahl, Marten Bolin
            Date: 2017-11-17
            Last update:
            Purpose: Make Insert of Feedback to the database
            :param user_id : The id of the user that has made the rating or watched
            :type int
            :param movie_id : The id of the movie that has been rated or watched
            :type int
            :param watched : 1 if has watched (optional)
            :type int
            :param rating : the rating that was made, 1-5 (optional)
            :type float
            """
            InsertFeedback().insert_feedback(user_id, movie_id, watched, rating)

            if rating:
                path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                model = generate_model.load_model(path + '/model/new_model.sav')
                # Converting to lists because of coo_matrix
                rating_list = [rating]
                user_list = [user_id]
                movie_list = [movie_id]

                # Need to define shape so that it is coherent with the previous model
                user_matrix = sp.coo_matrix((rating_list, (user_list, movie_list)),
                                            shape=(RetrieveUser().retrieve_largest_user_id(),
                                                   RetrieveMovie().retrieve_largest_movie_id()+1))
                generate_model.evolve_model(path + '/model/new_model.sav', model, user_matrix)
