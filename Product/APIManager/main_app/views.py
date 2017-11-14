
"""
This module contains classes that handle the API requests
"""
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Product.RecommendationManager.Recommendation.recommendation import Recommendation

class RecommendationsView(APIView):
    """
    This class is used to return the top 10 recommendations from Recommendations
    """
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        This function handles get requests to the server and returns a browsable API if gone
        directly to in the browser.
        """

        recs = Recommendation(55, 10).generate_recommendation_list().__dict__
        return Response(recs)

#def recommendations(request):
 #   recs = {"movies":[
  #      {"name":"Batman","id":1},
   #     {"name":"Horseman","id":2},
    #    {"name":"Birdperson","id":3},
     #   {"name":"Manman","id":4},
      #  {"name":"Cowman","id":5},
       # {"name":"Snakeman","id":6},
        #{"name":"Butterflyman","id":7},
        #{"name":"The extremely ordinary man","id":8},
        #{"name":"Wonderman the movie","id":9},
        #{"name":"Manbat","id":10},
        #]}
    #recs= {"name":"Batman","id":1}
    #return JsonResponse(recs)

def trending(request):
    recs = {"trendingMovies":[
        {"name":"Batmantredning","id":1},
        {"name":"Horseman","id":2},
        {"name":"Birdperson","id":3},
        {"name":"Manman","id":4},
        {"name":"Cowman","id":5},
        {"name":"Snakeman","id":6},
        {"name":"Butterflyman","id":7},
        {"name":"The extremely ordinary man","id":8},
        {"name":"Wonderman the movie","id":9},
        {"name":"Manbat","id":10},
        ]}
    #recs= {"name":"Batman","id":1}
    return JsonResponse(recs)


def youtubetrending(request):
    recs = {"youtubeMovies":[
        {"name":"Batmanyoutubetrending","id":1},
        {"name":"Horseman","id":2},
        {"name":"Birdperson","id":3},
        {"name":"Manman","id":4},
        {"name":"Cowman","id":5},
        {"name":"Snakeman","id":6},
        {"name":"Butterflyman","id":7},
        {"name":"The extremely ordinary man","id":8},
        {"name":"Wonderman the movie","id":9},
        {"name":"Manbat","id":10},
        ]}
    #recs= {"name":"Batman","id":1}
    return JsonResponse(recs)

def twittertrending(request):
    recs = {"twitterMovies":[
        {"name":"Batmantwittertrending","id":1},
        {"name":"Horseman","id":2},
        {"name":"Birdperson","id":3},
        {"name":"Manman","id":4},
        {"name":"Cowman","id":5},
        {"name":"Snakeman","id":6},
        {"name":"Butterflyman","id":7},
        {"name":"The extremely ordinary man","id":8},
        {"name":"Wonderman the movie","id":9},
        {"name":"Manbat","id":10},
        ]}
    #recs= {"name":"Batman","id":1}
    return JsonResponse(recs)
