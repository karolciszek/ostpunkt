from django.db import models
from django.conf import settings

# Create your models here.
class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    set_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None)

    def __str__(self):
        return '[({}, {}) at {} by {}]'.format(self.lat,
                                               self.lng,
                                               self.set_at,
                                               self.author)
