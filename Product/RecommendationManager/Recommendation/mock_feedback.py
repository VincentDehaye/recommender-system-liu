"""
creating some mock feedback to add to the database
"""
from Product.RecommendationManager.Recommendation.feedback import Feedback

user_ids = [1, 1, 1, 1, 2, 2, 3, 3, 4, 4]
movie_ids = [1, 2, 5, 4, 2, 4, 3, 6, 4, 8]
watched = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
ratings = [5, 4, 3, 2, 1, 3, 4, 5, 2, 1]

for mock in zip(user_ids, movie_ids, watched, ratings):
    Feedback().insert_feedback(mock[0], mock[1], mock[2], mock[3])

