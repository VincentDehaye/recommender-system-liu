"""
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-15
    Last update: 2017-11-23
    Purpose:
    This module populates the database with recommendations for users.
"""
import time
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation


class CreateRecommendationsForAllUsers:
    """
    Author: Alexander Dahl, Marten Bolin
    Date: 2017-11-15
    Last update: 2017-11-15
    Purpose:
    This module populates the database with recommendations for all users
    """
    @staticmethod
    def execute(number_of_users=None):
        """
        Author: Alexander Dahl, Marten Bolin
        Date: 2017-11-15
        Last update: 2017-11-13
        Purpose:
        This fucntion populates the database with recommendations for all users.
        :param number_of_users : how many users to create recommendations for
        """
        users = RetrieveUser().retrieve_all_users()
        if not number_of_users:
            number_of_users = len(users)
        # populates the database with all the recommendations for all users
        for user, user_number in zip(users, range(0, number_of_users)):
            # the Recommendation class will insert it to the database when it is generated
            Recommendation(user.id, 10).generate_recommendation_list()
