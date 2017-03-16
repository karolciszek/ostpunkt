from django.db import models

# Create your models here.
class Point(models.Model):
    lat = models.FloatField()
    lng = models.FloatField()
    set_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=150, default="")
