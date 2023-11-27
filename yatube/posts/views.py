from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def index(request):
    latest = Post.objects.all()[:10]

    output = []
    # TODO I do not understand how does it know which DB to search from.

    for item in latest:
        output.append(item.text+'\n')
    return HttpResponse(output)

# Create your views here.
