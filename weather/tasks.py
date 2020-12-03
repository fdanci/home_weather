from celery import shared_task

from django.core.mail import send_mail

from decouple import config

from .models import Settings


@shared_task
def send_email_task():
    # url = 
    # response = requests.request("GET", url)

    settings = Settings.objects.all()[0]
    message = f'location {settings.location}\n' \
              f'frequency {settings.frequency}\n' \
              f'hour {settings.hour}'
    send_mail('Test settings email task',
              message,
              config('EMAIL'),
              ['florin.danci96@gmail.com'])
    return None
