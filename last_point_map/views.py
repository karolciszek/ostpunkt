from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Point

# Create your views here.
def get_recent_point(request):
    return HttpResponse(serializers.serialize('json', [Point.objects.last()]))
