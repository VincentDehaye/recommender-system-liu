"""
    Author: Alexander Dahl
    Date: 2017-11-15
    Last update: 2017-11-15
    Purpose:
    This module populates the database with recommendations for all users.
"""
from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

USERS = RetrieveUser().retrieve_all_users()

# populates the database with all the recommendations for all users
for user in USERS:
    # generates a recommendation list of 10 for a user
    recommendations = Recommendation(user.id, 10).generate_recommendation_list().__dict__
    # Creates an instance of InsertRecommendation that handles database insertions.
    # Calls the insert_recommendation method in it and makes the db insertion
    InsertRecommendation().insert_recommendation(user_id=user.id,
                                                 movie_list=recommendations['recommendation_list'])
