from celery import shared_task

from django.core.mail import send_mail

from decouple import config

from .models import Settings


@shared_task
def send_email_task():
    settings = Settings.objects.all()[0]
    send_mail('Test settings email task',
              f'location {settings.location}',
              f'frequency {settings.frequency}',
              f'hour {settings.hour}',
              config('EMAIL'),
              ['florin.danci96@gmail.com'])
    return None
