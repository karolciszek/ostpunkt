from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.map_page, name="map_page"),
    url(r'^submit$', views.submit_point),
    url(r'^get_recent$', views.get_recent_point, name="get_recent_point")
]
