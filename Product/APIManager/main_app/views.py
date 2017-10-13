from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("Hello, world!")

def recommendations(request):
    recs = {"movies":["batman","dasd"]}
    return JsonResponse(recs)
