from Product.Database.DatabaseManager.Insert.InsertRecommendation import InsertRecommendation
from Product.Database.DatabaseManager.Retrieve.RetrieveUser import RetrieveUser
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

users = RetrieveUser().retrieve_all_users()

for user in users:
    print(user.id)
    recommendations=Recommendation(user.id, 10).generate_recommendation_list().__dict__

#    print(recommendations.get('recommendation_list'))
    for rec in recommendations.get('recommendation_list'):
        print(rec['id'])
        print(user.id)
        # TODO this method is broken at the moment, will be fixed soon
        #InsertRecommendation().insert_recommendation(user_id=user.id, movie_id=rec['id'])
        print('inserted')
