from django.test import TestCase

from weather.shared.forecast import Forecast
from weather.shared.forecast_5days import Forecast5days


class TestForecast5Days(TestCase):
    """Test cases for Forecast object"""

    def test_forecast_cosna(self):
        """Test if the forecast is created successfully."""
        forecast: Forecast5days = Forecast.get_forecast_5days('cosna')
        self.assertIsInstance(forecast, Forecast5days)

    def test_forecast_vatra_dornei(self):
        """Test if the forecast is created successfully."""
        forecast: Forecast5days = Forecast.get_forecast_5days('vatra_dornei')
        self.assertIsInstance(forecast, Forecast5days)

    def test_forecast_ilisesti(self):
        """Test if the forecast is created successfully."""
        forecast: Forecast5days = Forecast.get_forecast_5days('ilisesti')
        self.assertIsInstance(forecast, Forecast5days)
