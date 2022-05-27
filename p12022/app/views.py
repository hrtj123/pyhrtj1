from django.shortcuts import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def home(request):
    return HttpResponse("Hello")
