from django.test import TestCase
from django.contrib.auth import get_user_model
import json
from .models import Point
from .views import get_recent_point

User = get_user_model()

# Create your tests here.
class RecentPointTestCase(TestCase):
    def setUp(self):
        self.u = User(username="test")
        self.u.save()

        self.pt = Point(
            lat=24.4,
            lng=2.30,
            author=self.u
        )
        self.pt.save()

    def tearDown(self):
        self.pt.delete()
        self.u.delete()

