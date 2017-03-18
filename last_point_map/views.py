from django.shortcuts import render
from django.http import HttpResponse
from .models import Point

# Create your views here.
def get_recent_point(request):
    return HttpResponse(Point.objects.latest())
