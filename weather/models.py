from django.db import models


class Forecast(models.Model):
    """An entity that holds information 5 days worth"""

    forecast = models.CharField(max_length=30000, default='None')
    date = models.CharField(max_length=10, default='None')
    location = models.CharField(max_length=20, default='None')

    class Meta:
        verbose_name_plural = 'forecasts'
