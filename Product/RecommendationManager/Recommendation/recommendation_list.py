"""
Class to get the correct output structure in the
recommendation.generate_recommendation_list()
"""
class RecommendationList(object):
    """
    Constructor
    """
    def __init__(self, user_id, recommendation_list):
        self.user_id = user_id
        self.recommendation_list = recommendation_list
