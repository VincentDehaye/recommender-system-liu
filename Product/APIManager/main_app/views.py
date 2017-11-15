
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
from Product.DataManager.TopTrending.RetrieveTopTrendingTotal import RetrieveTopTrendingTotal
from Product.DataManager.TopTrending.RetrieveTopTrendingTwitter import RetrieveTopTrendingTwitter
from Product.DataManager.TopTrending.RetrieveTopTrendingYoutube import RetrieveTopTrendingYoutube


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
                {"title":"Batman", "id":1},
                {"title":"Horseman", "id":2},
                {"title":"Birdperson", "id":3},
                {"title":"Manman", "id":4},
                {"title":"Cowman", "id":5},
                {"title":"Snakeman", "id":6},
                {"title":"Butterflyman", "id":7},
                {"title":"The extremely ordinary man", "id":8},
                {"title":"Wonderman the movie", "id":9},
                {"title":"Manbat", "id":10},
                ]}
        except:
            traceback.print_exc()
            recs = {"movies":[
                {"title":"Batman", "id":1},
                {"title":"Horseman", "id":2},
                {"title":"Birdperson", "id":3},
                {"title":"Manman", "id":4},
                {"title":"Cowman", "id":5},
                {"title":"Snakeman", "id":6},
                {"title":"Butterflyman", "id":7},
                {"title":"The extremely ordinary man", "id":8},
                {"title":"Wonderman the movie", "id":9},
                {"title":"Manbat", "id":10},
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
        try:
            trender = RetrieveTopTrendingTotal()
            recs = {"trendingMovies": trender.get_top_trending(10).list()}
        except:
            recs = {"trendingMovies":[
                {"title":"Batmantredning", "score":1},
                {"title":"Horseman", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)


class YoutubeTrendingView(APIView):

    def get(self, request):
        try:
            trender = RetrieveTopTrendingYoutube()
            recs = {"youtubeMovies": trender.get_top_trending(10).list()}
        except:
            recs = {"youtubeMovies":[
                {"title":"Batmanyoutubetrending", "score":1},
                {"title":"Horseman", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)

class TwitterTrendingView(APIView):

    def get(self, request):
        try:
            trender = RetrieveTopTrendingTwitter()
            recs = {"twitterMovies": trender.get_top_trending(10).list()}
        except:
            recs = {"twitterMovies":[
                {"title":"Batmantwittertrending", "score":1},
                {"title":"Horseman", "score":2},
                {"title":"Birdperson", "score":3},
                {"title":"Manman", "score":4},
                {"title":"Cowman", "score":5},
                {"title":"Snakeman", "score":6},
                {"title":"Butterflyman", "score":7},
                {"title":"The extremely ordinary man", "score":8},
                {"title":"Wonderman the movie", "score":9},
                {"title":"Manbat", "score":10},
                ]}
        return Response(recs)

class RateMovieView(APIView):
    serializer_class = RatingSerializer

    def post(self, request):
        serializer = RatingSerializer(request.data)
        print(serializer.data)
        return Response(serializer.data)
