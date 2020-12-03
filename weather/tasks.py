from celery import shared_task

from django.core.mail import send_mail

from decouple import config

from .models import Settings


@shared_task
def send_email_task():
    # settings = Settings.objects.all()[0]
    # send_mail('Celery Task Worked!',
    #           'This is the proof the task worked!',
    #           config('EMAIL'),
    #           ['florin.danci96@gmail.com'])
    return None
