

from django.http import HttpResponse


def homeView(request):
    return HttpResponse('Django rest API')