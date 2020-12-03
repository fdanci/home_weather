from celery import shared_task

from django.core.mail import send_mail

from decouple import config

import requests

from .models import Settings


@shared_task
def send_email_task():
    requests.request("GET", config('BLANK_URL'))

    settings = Settings.objects.all()[0]

    message = f'location {settings.location}\n' \
              f'frequency {settings.frequency}\n' \
              f'hour {settings.hour}'

    if settings.alarm_status == 'on':
        send_mail('ON',
                  message,
                  config('EMAIL'),
                  ['florin.danci96@gmail.com'])
    else:
        send_mail('OFF',
                  message,
                  config('EMAIL'),
                  ['florin.danci96@gmail.com'])
    return None
