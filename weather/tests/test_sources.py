from django.test import TestCase
from weather.weather_sources.source_1 import Source1


class TestSource1(TestCase):
    """Test forecasting for 'weather_sources.source_1.py'."""

    def test_today(self):
        """Does this method return status code 200?"""
        response = Source1.today()
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days(self):
        """Does this method return status code 200?"""
        response = Source1.forecast_5days()
        self.assertEquals(response.status_code, 200)
