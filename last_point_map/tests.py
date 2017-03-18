from django.test import TestCase
from .models import Point
from .views import get_recent_point

# Create your tests here.
class RecentPointTestCase(TestCase):
    def setUp(self):
        self.pt = Point(
            lat=24.4,
            lng=2.30
        )
        self.pt.save()

    def tearDown(self):
        self.pt.delete()
