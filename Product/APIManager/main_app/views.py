from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def recommendations(request):
    recs = {"movies":[
        {"name":"Batman","id":1},
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
