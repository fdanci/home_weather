from celery import shared_task

from django.core.mail import send_mail

from decouple import config


@shared_task
def send_email_task():
    send_mail('Celery Task Worked!',
              'This is the proof the task worked!',
              config('EMAIL'),
              ['florin.danci96@gmail.com'])
    return None
