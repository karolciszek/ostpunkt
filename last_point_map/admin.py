from django.contrib import admin
from .models import Point
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
admin.site.register(Point, LeafletGeoAdmin)
