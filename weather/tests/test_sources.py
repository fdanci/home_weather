from django.test import TestCase
from weather.weather_sources.source_1 import Source1


class TestSource1(TestCase):
    """Test forecasting for 'weather_sources.source_1.py'."""

    def test_today_cosna(self):
        """Does this method, Coșna location, return status code 200?"""
        response = Source1.today('280811')
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days_cosna(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_5days('280811')
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days_vd(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_5days('275841')
        self.assertEquals(response.status_code, 200)

    def test_forecast_5days_ilisesti(self):
        """Does this method, Ilisesti location, return status code 200?"""
        response = Source1.forecast_5days('280883')
        self.assertEquals(response.status_code, 200)

    def test_forecast_12hours_vd(self):
        """Does this method, Vatra Dornei location, return status code 200?"""
        response = Source1.forecast_12hours('275841')
        self.assertEquals(response.status_code, 200)

    def test_forecast_12hours_cosna(self):
        """Does this method, Cosna location, return status code 200?"""
        response = Source1.forecast_12hours('280811')
        self.assertEquals(response.status_code, 200)

    def test_forecast_12hours_ilisesti(self):
        """Does this method, Ilisesti location, return status code 200?"""
        response = Source1.forecast_12hours('280883')
        self.assertEquals(response.status_code, 200)
