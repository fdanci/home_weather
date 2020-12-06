from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Settings
from .shared.date_util import DateUtil

import logging

from .shared.forecast import Forecast

logger = logging.getLogger(__name__)

from decouple import config
from twilio.rest import Client

client = Client(config('ACCOUNT_SID_TWILIO'), config('AUTH_TOKEN_TWILIO'))


@shared_task
def send_alarm_task():
    settings = Settings.objects.all()[0]
    # Store app settings, read from database, into variables.
    settings_day_list = settings.day.split(',')
    is_email_alarm = settings.alarm_status == 'on'
    is_sms_alarm = settings.alarm_status_sms == 'on'
    location = settings.location

    # If any alarm on, try sending alarm in case bad weather ahead.
    if (is_email_alarm or is_sms_alarm) and DateUtil.get_day_today() in settings_day_list:
        try:
            forecast_5days = Forecast.read_forecast(location)
        except Exception as err:
            logger.error('send_alarm_task')
            logger.error(err)
        else:
            if forecast_5days.has_precipitations():  # If bad weather, send alarms.
                message = forecast_5days.get_message()
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
def wake_up_task():
    """Keep app awake all the time."""
    try:
        requests.request("GET", config('BLANK_URL'))
    except Exception as err:
        logger.error('wake_up_task')
        logger.error(err)
