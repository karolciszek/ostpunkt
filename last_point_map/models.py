from django.db import models
from django.conf import settings
from math import isclose

# Create your models here.
class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    set_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)
    zoom = models.IntegerField(default=10)

    def set_at_readable(self):
        return self.set_at.strftime('%H:%M:%S on %Y-%m-%d')

    def __str__(self):
        return '[({}, {}) at {} by {}, zoom {}]'.format(self.lat,
                                                        self.lng,
                                                        self.set_at_readable,
                                                        self.author,
                                                        self.zoom)

    def __eq__(self, other):
        if type(other) is type(self):
            return (isclose(float(self.lat), float(other.lat))
                    and isclose(float(self.lng), float(other.lng))
                    and self.zoom == other.zoom)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
