from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

users=RetrieveUser().retrieve_all_users()
for user in users:
    print(user.id)
#    print(Recommendation(user.id, 10).generate_recommendation_list().__dict__)

#InsertRecommendation().insert_recommendation()

