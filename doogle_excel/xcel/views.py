from django.http import HttpResponse


def index(request):
    return HttpResponse("<b>Shortly open the excel website.</b>")

