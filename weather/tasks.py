from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Settings, Forecast
from .shared.date_util import DateUtil
from .shared.forecast_5days import Forecast5days

import logging

logger = logging.getLogger(__name__)

from decouple import config
from twilio.rest import Client

client = Client(config('ACCOUNT_SID_TWILIO'), config('AUTH_TOKEN_TWILIO'))


@shared_task
def send_email_task():
    settings = Settings.objects.all()[0]

    settings_day_list = settings.day.split(',')
    today = DateUtil.get_day_today()

    is_email_alarm = settings.alarm_status == 'on'
    is_sms_alarm = settings.alarm_status_sms == 'on'

    # If any alarm on, try sending alarm in case bad weather ahead.
    if (is_email_alarm or is_sms_alarm) and today in settings_day_list:
        try:
            today_forecasts: list[Forecast] = Forecast.objects.filter(location=settings.location,
                                                                      date=DateUtil.get_date_today())
            # If forecast data exists, create 'Forecast' object from it.
            if today_forecasts:
                today_forecast = today_forecasts[0]
                forecast: Forecast5days = Forecast5days(settings.location, raw_data=today_forecast.forecast)
            else:  # Else request the API for data.
                forecast: Forecast5days = Forecast5days(settings.location)
        except Exception as err:
            logger.error('tasks.send_email_task')
            logger.error(err)
        else:
            if forecast.has_precipitations():
                message = f"{forecast.headline}\n" \
                          f"Minimă: {forecast.min_temperature[0]} \N{DEGREE SIGN}C ({forecast.min_temperature[1]})\n" \
                          f"Maximă: {forecast.max_temperature[0]} \N{DEGREE SIGN}C ({forecast.max_temperature[1]})\n\n" \
                          f"{forecast.days_that_rain()}"

                # Send alarms to target.
                if is_email_alarm:
                    send_email_alarm(message)
                if is_sms_alarm:
                    send_sms_alarm(message)
    return None


def send_email_alarm(message: str):
    """Send email notification."""
    send_mail('Vreme rea de polog',
              message,
              config('EMAIL'),
              ['florin.danci96@gmail.com'])


def send_sms_alarm(message: str):
    """Send sms notification."""
    client.messages.create(to=config('TARGET_PHONE_1'),
                           from_="+14434874065",
                           body=message)


@shared_task
def wake_up():
    """Keep app awake all the time."""
    requests.request("GET", config('BLANK_URL'))
