from django.db import models
from django.conf import settings
from math import isclose
from djgeojson.fields import PointField

# Create your models here.
class Point(models.Model):
    # lat = models.FloatField()
    # lng = models.FloatField()
    point = PointField()
    set_at = models.DateTimeField(auto_now=True)
    arrival = models.DateTimeField()
    description = models.TextField(default="No comment")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)
    zoom = models.IntegerField(default=6)

    def __str__(self):
        return '{} at {}'.format(
            self.point['coordinates'],
            self.arrival
        )

    def coords_to_str(self):
        return '{}, {}'.format(
            round(self.point['coordinates'][1], 3),
            round(self.point['coordinates'][0], 3)
        )

    # def __eq__(self, other):
    #     if type(other) is type(self):
    #         return (isclose(float(self.lat), float(other.lat))
    #                 and isclose(float(self.lng), float(other.lng))
    #                 and int(self.zoom) == int(other.zoom))
    #     else:
    #         return False

    # def __ne__(self, other):
    #     return not self.__eq__(other)
