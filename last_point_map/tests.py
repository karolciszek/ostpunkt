from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
import json
from .models import Point
from .views import get_recent_point, submit_point, map_page

User = get_user_model()
data = {'lat': 34.0, 'lng': 45.3, 'zoom': 13}

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
        response = self.c.get(reverse(submit_point), {'lat': 34.0, 'lng': 45.3, 'zoom': 13})
        self.assertEqual(response.status_code, 403)

    def test_logged_in(self):
        """User logged in returns 200"""
        self.c.force_login(self.u)
        response = self.c.get(reverse(submit_point), {'lat': 34.0, 'lng': 45.3, 'zoom': 13})
        self.assertEqual(response.status_code, 200)

    def test_model_inst_created(self):
        """A model instance is created and saved correctly"""
        self.c.force_login(self.u)
        response = self.c.get(reverse(submit_point), data)
        self.assertEqual(Point.objects.last().lat, data['lat'])

    def test_same_point_not_submitted(self):
        """The same point is not submitted twice"""
        self.c.force_login(self.u)
        data = {'lat': 34.0, 'lng': 45.3, 'zoom': 13}
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        response = self.c.get(reverse(submit_point), data)
        self.assertEqual(Point.objects.count(), 1)


class MapPageTestCase(TestCase):
    def setUp(self):
        credentials = {'username': 'test', 'password': 'probowanie'}
        self.u = User(**credentials)
        self.u.save()
        self.c = Client()

    def tearDown(self):
        self.u.delete()

    def test_not_logged_in(self):
        """User not logged in returns 200"""
        response = self.c.get(reverse(map_page), {'lat': 34.0, 'lng': 45.3})
        self.assertEqual(response.status_code, 200)

    def test_logged_in(self):
        """User logged in returns 200"""
        self.c.force_login(self.u)
        response = self.c.get(reverse(map_page), {'lat': 34.0, 'lng': 45.3})
        self.assertEqual(response.status_code, 200)

class PointTestCase(TestCase):
    def setUp(self):
        credentials = {'username': 'test', 'password': 'probowanie'}
        self.u = User(**credentials)
        self.u.save()
        self.a = Point(
            lat=23.4,
            lng=23.1,
            author=self.u
        )

    def tearDown(self):
        self.u.delete()

    def test_equal(self):
        """The expressiont pt == pt returns True"""
        self.assertTrue(self.a == self.a)
        self.assertFalse(self.a != self.a)

    def test_almost_equal(self):
        """The expression pt1 == pt2 returns True when pt1 is close to pt2"""
        x = Point(
            lat=23.4,
            lng=23.1,
            author=self.u
        )
        self.assertTrue(self.a == x)
        self.assertFalse(self.a != x)

    def test_not_equal(self):
        """The expression pt1 == pt2 returns False when pt1 is not close to pt2"""
        x = Point(
            lat=24.4,
            lng=23.1,
            author=self.u
        )
        self.assertFalse(self.a == x)
        self.assertTrue(self.a != x)
