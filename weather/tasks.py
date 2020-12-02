from celery import shared_task

from django.core.mail import send_mail


@shared_task
def send_email():
    send_mail('Celey Task Worked!',
              'This is the proof the task worked!',
              'florin.danci96@gmail.com',
              ['florin.danci96@gmail.com'])
    return None
