from celery import shared_task

from django.core.mail import send_mail

from decouple import config

import requests

from .models import Settings, Forecast
from .shared.date_util import DateUtil
from .shared.forecast_5days import Forecast5days


@shared_task
def send_email_task():
    # First make sure to keep the server awake by pinging itself.
    requests.request("GET", config('BLANK_URL'))

    settings = Settings.objects.all()[0]

    try:
        today_forecasts: Forecast = Forecast.objects.filter(location=settings.location, date=DateUtil.get_date_today())

        # If forecast data exists, create 'Forecast' object from it.
        if today_forecasts:
            today_forecast = today_forecasts[0]
            forecast: Forecast5days = Forecast5days(settings.location, raw_data=today_forecast.forecast)
        else:
            forecast: Forecast5days = Forecast5days(settings.location)
    except Exception:
        pass
    else:
        if settings.alarm_status == 'on' and not forecast.has_precipitations():
            message = f"{forecast.headline}\n" \
                      f"Minimă: {forecast.min_temperature}" \
                      f"Maximă: {forecast.min_temperature}"

            send_mail('Vreme rea',
                      message,
                      config('EMAIL'),
                      ['florin.danci96@gmail.com'])
    return None
