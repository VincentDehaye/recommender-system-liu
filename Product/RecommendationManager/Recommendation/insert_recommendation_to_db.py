from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

users = RetrieveUser().retrieve_all_users()

# populates the database with all the recommendations for all users
for user in users:
    recommendations = Recommendation(user.id, 10).generate_recommendation_list().__dict__
    InsertRecommendation().insert_recommendation(user_id=user.id,
                                                 movie_list=recommendations['recommendation_list'])
