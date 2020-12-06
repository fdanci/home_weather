import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home_weather.settings')

app = Celery('home_weather')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-every-day': {
        'task': 'weather.tasks.send_alarm_task',
        'schedule': crontab(
            minute='0',
            hour='8,16,17,18,19,20',
            day_of_week=[0, 1, 2, 3, 4, 5, 6]
        )
    },
    'every-29-minutes': {
        'task': 'weather.tasks.wake_up_task',
        'schedule': crontab(minute='*/29')
    },
}

app.conf.timezone = 'Europe/Bucharest'

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
