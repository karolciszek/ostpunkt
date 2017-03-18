from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.core import serializers
from .models import Point

# Create your views here.
def get_recent_point(request):
    return HttpResponse(serializers.serialize('json', [Point.objects.last()]))

def submit_point(request):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    point = Point(
        lat=request.GET['lat'],
        lng=request.GET['lng'],
        author=request.user
    )
    point.save()

    return HttpResponse()
