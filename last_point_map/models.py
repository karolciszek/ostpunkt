from django.db import models
from django.conf import settings
from math import isclose

# Create your models here.
class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    set_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)

    def __str__(self):
        return '[({}, {}) at {} by {}]'.format(self.lat,
                                               self.lng,
                                               self.set_at.strftime('%H:%M:%S on %Y-%m-%d'),
                                               self.author)

    def __eq__(self, other):
        if type(other) is type(self):
            return isclose(self.lat, other.lat) and isclose(self.lng, other.lng)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
