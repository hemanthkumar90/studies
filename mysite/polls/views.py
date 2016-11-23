from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Saibaba Trust, Welcome you all.")