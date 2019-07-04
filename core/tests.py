from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Launchpad
from core.serializers import LaunchpadSerializer

LAUNCHPADS_URL = reverse('launchpadview')


class LaunchpadsApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_retrieve_launchpad_list(self):
        """Test retrieving a list of launchpads"""
        res = self.client.get(LAUNCHPADS_URL)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        if res.data and isinstance(res.data, list):
            self.assertTrue(len(res.data) > 0)
