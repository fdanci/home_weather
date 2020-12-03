from django.db import models


class Forecast(models.Model):
    """An entity that holds information 5 days or 12 hours worth."""

    forecast = models.CharField(max_length=30000, default='None')
    date = models.CharField(max_length=20, default='None')
    location = models.CharField(max_length=20, default='None')

    class Meta:
        verbose_name_plural = 'forecasts'


class Settings(models.Model):
    """Single entity holding information about worker beat interval."""

    # The location where the forecast conditions are checked.
    location = models.CharField(max_length=10, default='cosna')
    # 1 - Monday, 2 - Tuesday, etc.
    frequency = models.CharField(max_length=20, default='1')
    # The hour at which the beat starts.
    hour = models.CharField(max_length=20, default='08h00')
