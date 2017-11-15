
"""
Author: Bamse
Date: 2017-09-26
Last update: 2017-11-14 by Bamse
This module contains all the view classes that handle API requests.
"""
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import traceback

from main_app.serializers import RatingSerializer
from Product.RecommendationManager.Recommendation.recommendation import Recommendation
from Product.DataManager.TopTrending.RetrieveTopTrendingTwitter import RetrieveTopTrendingTwitter

class RecommendationsView(APIView):
    """
    Author: Bamse
    Date: 2017-10-04
    Last update: 2017-11-14 by Bamse
    This class is used to return the top 10 recommendations from Recommendations team
    """
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        """
        Author: Bamse
        Date: 2017-11-14
        Last update: 2017-11-14 by Bamse
        Purpose: Handles GET requests to recommendations API. Returns mock data if fetching from
        recommendation doesn't work.
        """
        try:
            recs = Recommendation(55, 10).generate_recommendation_list().__dict__
        except ValueError:
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
        except:
            traceback.print_exc()
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

class TrendingView(APIView):

    def get(self, request):
        """
        Author: Bamse
        Date: 2017-11-14
        Last update: 2017-11-14 by Bamse
        Purpose: Handles GET requests to trending API. Returns mock data.
        """
        recs = {"trendingMovies":[
            {"name":"Batmantredning", "id":1},
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


class YoutubeTrendingView(APIView):

    def get(self, request):
        recs = {"youtubeMovies":[
            {"name":"Batmanyoutubetrending", "id":1},
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

class TwitterTrendingView(APIView):

    def get(self, request):
        try:
            trender = RetrieveTopTrendingTwitter()
            recs = trender.get_top_trending(10).dict()
        except:
            recs = {"twitterMovies":[
                {"name":"Batmantwittertrending", "id":1},
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

class RateMovieView(APIView):
    serializer_class = RatingSerializer

    def post(self, request):
        serializer = RatingSerializer(request.data)
        print(serializer.data)
        return Response(serializer.data)
