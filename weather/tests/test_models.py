from django.test import TestCase

from weather.models import Forecast


class TestForecast(TestCase):
    """Test cases for Forecast model"""

    @classmethod
    def setUpTestData(cls):
        with open('weather/tests/cosna.json', 'r') as f:
            cosna_json = f.read()

        Forecast.objects.create(
            forecast=cosna_json,
            date='2020-12-10',
            location='cosna'
        )

    def test_forecast_label(self):
        forecast = Forecast.objects.get(id=1)
        forecast_label = forecast._meta.get_field('forecast').verbose_name
        self.assertEqual(forecast_label, 'forecast')

    def test_date_label(self):
        forecast = Forecast.objects.get(id=1)
        forecast_label = forecast._meta.get_field('date').verbose_name
        self.assertEqual(forecast_label, 'date')

    def test_location_label(self):
        forecast = Forecast.objects.get(id=1)
        forecast_label = forecast._meta.get_field('location').verbose_name
        self.assertEqual(forecast_label, 'location')

    def test_forecast_max_length(self):
        forecast = Forecast.objects.get(id=1)
        max_length = forecast._meta.get_field('forecast').max_length
        self.assertEqual(max_length, 30000)

    def test_date_max_length(self):
        forecast = Forecast.objects.get(id=1)
        max_length = forecast._meta.get_field('date').max_length
        self.assertEqual(max_length, 20)

    def test_location_max_length(self):
        forecast = Forecast.objects.get(id=1)
        max_length = forecast._meta.get_field('location').max_length
        self.assertEqual(max_length, 20)
