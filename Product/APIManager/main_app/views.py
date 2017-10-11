from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def recommendations(request):
    recs = {"1": "Zorro"}
    return JsonResponse(recs)
