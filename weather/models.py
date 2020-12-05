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
    location = models.CharField(max_length=20, default='cosna')
    # 0 - Monday, 1 - Tuesday, etc. Can be multiple days separated by comma, e.g. 1,3,4,5.
    day = models.CharField(max_length=20, default='0')
    # The hour at which the beat starts.
    hour = models.CharField(max_length=20, default='5')

    alarm_status = models.CharField(max_length=4, default='off')
