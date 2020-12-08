from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Tests all views."""

    def test_cosna(self):
        """Test if requests work for this page."""
        response = self.client.get('/cosna/')
        self.assertEqual(response.status_code, 200)

    def test_vatra_dornei(self):
        """Test if requests work for this page."""
        response = self.client.get('/vatra_dornei/')
        self.assertEqual(response.status_code, 200)

    def test_ilisesti(self):
        """Test if requests work for this page."""
        response = self.client.get('/ilisesti/')
        self.assertEqual(response.status_code, 200)

    def test_blank(self):
        """Test if requests work for this page."""
        response = self.client.get('/blank/')
        self.assertEqual(response.status_code, 200)
