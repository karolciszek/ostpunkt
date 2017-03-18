from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
from .models import Point
from .views import get_recent_point, submit_point

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

    def test_lat_preserved(self):
        """Lat attribute is the same when deserialised"""
        response = get_recent_point(None)
        fields = json.loads(response.content.decode('utf-8'))[0]['fields']
        self.assertAlmostEqual(fields['lat'], self.pt.lat)

    def test_lng_preserved(self):
        """Lng attribute is the same when deserialised"""
        response = get_recent_point(None)
        fields = json.loads(response.content.decode('utf-8'))[0]['fields']
        self.assertAlmostEqual(fields['lng'], self.pt.lng)

class SubmitPointTestCase(TestCase):
    def setUp(self):
        credentials = {'username': 'test', 'password': 'probowanie'}
        self.u = User(**credentials)
        self.u.save()
        self.c = Client()

    def tearDown(self):
        self.u.delete()

    def test_not_logged_in(self):
        """User not logged in returns 403"""
        response = self.c.get(reverse(submit_point), {'lat': 34.0, 'lng': 45.3})
        self.assertEqual(response.status_code, 403)
