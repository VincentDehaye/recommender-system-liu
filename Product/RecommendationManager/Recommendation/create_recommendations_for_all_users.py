"""
    Author: Alexander Dahl
    Date: 2017-11-15
    Last update: 2017-11-15
    Purpose:
    This module populates the database with recommendations for all users.
"""
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation


class CreateRecommendationsForAllUsers:

    @staticmethod
    def execute():
        USERS = RetrieveUser().retrieve_all_users()

        # populates the database with all the recommendations for all users
        for user in USERS:
            # the Recommendation class will insert it to the database when it is generated
            Recommendation(user.id, 10).generate_recommendation_list()
