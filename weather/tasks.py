from celery import shared_task

from django.core.mail import send_mail

from decouple import config

import requests

from .models import Settings, Forecast
from .shared.date_util import DateUtil
from .shared.forecast_5days import Forecast5days


@shared_task
def send_email_task():
    settings = Settings.objects.all()[0]

    # If alarm is on, try sending alarm in case bad weather ahead.
    if settings.alarm_status == 'on':
        try:
            today_forecasts: Forecast = Forecast.objects.filter(location=settings.location,
                                                                date=DateUtil.get_date_today())

            # If forecast data exists, create 'Forecast' object from it.
            if today_forecasts:
                today_forecast = today_forecasts[0]
                forecast: Forecast5days = Forecast5days(settings.location, raw_data=today_forecast.forecast)
            else:  # Else request the API for data.
                forecast: Forecast5days = Forecast5days(settings.location)
        except Exception:
            pass
        else:
            if not forecast.has_precipitations():
                message = f"{forecast.headline}\n\n" \
                          f"Minimă: {forecast.min_temperature[0]} \N{DEGREE SIGN}C ({forecast.min_temperature[1]})\n" \
                          f"Maximă: {forecast.max_temperature[0]} \N{DEGREE SIGN}C ({forecast.max_temperature[1]})"

                send_mail('Vreme rea',
                          message,
                          config('EMAIL'),
                          ['florin.danci96@gmail.com'])
    return None


@shared_task
def wake_up():
    """Keep app awake all the time."""
    requests.request("GET", config('BLANK_URL'))
