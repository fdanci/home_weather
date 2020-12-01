from django.test import TestCase
from weather.weather_sources.source_1 import Source1


class TestSource1(TestCase):
    """Test forecasting for 'weather_sources.source_1.py'."""

    def test_today_cosna(self):
        """Does this method, Coșna location, return status code 200?"""
        response = Source1.today('cosna')
        self.assertEquals(response.status_code, 200)

    def test_today_vd(self):
        """Does this method, Coșna location, return status code 200?"""
        response = Source1.today('vatra_dornei')
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days_cosna(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_5days('cosna')
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days_vd(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_5days('vatra_dornei')
        self.assertEquals(response.status_code, 200)

    def test_forecast_12hours_vd(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_12hours('vatra_dornei')
        self.assertEquals(response.status_code, 200)

    def test_forecast_12hours_cosna(self):
        """Does this method, Cosna location, return status code 200?"""
        response = Source1.forecast_12hours('cosna')
        self.assertEquals(response.status_code, 200)
