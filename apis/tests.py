from django.test import TestCase
from django.test import Client
from django.conf import settings

# Create your tests here.

class BaseUnitTest(TestCase):

    def setUp(self):
        settings.DEBUG = False

    def test_math(self):
        self.assertEqual(2, 1+1)

    def tearDown(self):
        pass


class SimpleTests(TestCase):

    def setUp(self):
        settings.DEBUG = False

    def test_index(self):
        response = self.client.get('/index/')
        self.assertIn(response.status_code, (200, 302))

    def tearDown(self):
        pass
