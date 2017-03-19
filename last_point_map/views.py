from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.core import serializers
from .models import Point
try:
    from django.conf.settings import MAP_UNAUTHENTICATED_REDIRECT
except ImportError:
    MAP_UNAUTHENTICATED_REDIRECT = 'auth_login' # from django-registration

# Create your views here.
def map_page(request):
    if not request.user.is_authenticated():
        return redirect(MAP_UNAUTHENTICATED_REDIRECT)

    context = {
        'point': Point.objects.last()
    }
    return render(request, 'last_point_map/map.html', context=context)

def get_recent_point(request):
    if Point.objects.count() > 0:
        return HttpResponse(serializers.serialize('json', [Point.objects.last()]))
    else:
        return HttpResponse('[]')

def submit_point(request):
    if not request.user.is_authenticated():
        return HttpResponseForbidden()

    point = Point(
        lat=request.GET['lat'],
        lng=request.GET['lng'],
        zoom=request.GET['zoom'],
        author=request.user
    )

    if point != Point.objects.last():
        point.save()

    return HttpResponse()
