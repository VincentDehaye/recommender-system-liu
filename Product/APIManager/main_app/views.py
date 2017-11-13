
"""
This module contains classes that handle the API requests
"""

from rest_framework.response import Response
from rest_framework.views import APIView
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

class RecommendationsView(APIView):
    """
    This class is used to return the top 10 recommendations from Recommendations
    """

    def get(self, request):
        """
        This function handles get requests to the server and returns a browsable API if gone
        directly to in the browser.
        """

        recs = Recommendation(55, 10).generate_recommendation_list().__dict__
        return Response(recs)
