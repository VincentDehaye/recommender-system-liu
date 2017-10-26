from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def recommendations(request):
    recs = {"movies":[{"name":"Batman","id":1},{"name":"Horseman","id":2},{"name":"Birdperson","id":3},{"name":"Manman","id":4}]}
    #recs= {"name":"Batman","id":1}
    return JsonResponse(recs)
