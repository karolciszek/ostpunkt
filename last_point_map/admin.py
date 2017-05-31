from django.contrib import admin
from .models import Point
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class PointAdmin(LeafletGeoAdmin):
    settings_overrides = {
        'DEFAULT_ZOOM': 5,
        'DEFAULT_CENTER': (45.0, 25.0)
    }

    class Media:
        css = {
            'all': ('css/admin/admin-map.css',)
        }


admin.site.register(Point, PointAdmin)
