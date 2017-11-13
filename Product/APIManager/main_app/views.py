
"""
This module contains classes that handle the API requests
"""

from rest_framework.response import Response
from rest_framework.views import APIView

class RecommendationsView(APIView):
    """
    This class is used to return the top 10 recommendations.
    """

    def get(self, request):
        """
        This function handles get requests to the server and returns a browsable API if gone
        directly to in the browser.
        """

        recs = {"movies":[
            {"name":"Batman", "id":1},
            {"name":"Horseman", "id":2},
            {"name":"Birdperson", "id":3},
            {"name":"Manman", "id":4},
            {"name":"Cowman", "id":5},
            {"name":"Snakeman", "id":6},
            {"name":"Butterflyman", "id":7},
            {"name":"The extremely ordinary man", "id":8},
            {"name":"Wonderman the movie", "id":9},
            {"name":"Manbat", "id":10},
            ]}
        return Response(recs)
