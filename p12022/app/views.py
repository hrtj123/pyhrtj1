from django.shortcuts import HttpResponse
from django.views.decorators.http import require_safe


@require_safe
def home(request):
    return HttpResponse("Hello")
