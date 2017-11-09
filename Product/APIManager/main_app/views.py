from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


def index(request):
    return HttpResponse("Hello, world!")


class RecommendationsView(APIView):

    def get(self, request):
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
        #recs= {"name":"Batman","id":1}
        return Response(recs)
