web: gunicorn home_weather.wsgi --log-file -
worker: celery -A home_weather worker -l info