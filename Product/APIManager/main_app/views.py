from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def recommendations(request):
    recs = {"id":5,"name":"Batman"}
    return JsonResponse(recs)
