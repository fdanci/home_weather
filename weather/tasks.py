from celery import shared_task

from decouple import config
from twilio.rest import Client

from django.core.mail import send_mail

import requests

from .models import Settings
from .shared.date_util import DateUtil

import logging

from .shared.forecast import Forecast

logger = logging.getLogger(__name__)

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
    if is_email_alarm or is_sms_alarm and DateUtil.get_day_today() in settings_day_list:
        logger.info('Trying to send alarm...')
        try:
            forecast_5days = Forecast.get_forecast_5days(location)
        except Exception as err:
            logger.error('send_alarm_task')
            logger.error(err)
        else:
            if forecast_5days.has_precipitations():  # If bad weather, send alarms.
                message = forecast_5days.get_message()

                if is_email_alarm:
                    logger.info('Trying to send email...')
                    send_email_alarm(message)
                if is_sms_alarm:
                    logger.info('Trying to send sms...')
                    send_sms_alarm(message)
                logger.info('Alarm sent.')
            else:
                logger.info('Alarm not sent, weather looks good')
    return None


def send_email_alarm(message: str):
    """Send email notification."""
    send_mail('Vreme rea',
              message,
              config('EMAIL'),
              ['florin.danci96@gmail.com'])
    logger.info('Email sent.')


def send_sms_alarm(message: str):
    """Send sms notification."""
    client.messages.create(to=config('TARGET_PHONE_1'),
                           from_="+14434874065",
                           body=message)
    logger.info('Sms sent.')


@shared_task
def wake_up_task():
    """Keep app awake all the time."""
    try:
        requests.request("GET", config('BLANK_URL'))
    except Exception as err:
        logger.error('wake_up_task')
        logger.error(err)
