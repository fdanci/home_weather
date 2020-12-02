web: gunicorn home_weather.wsgi --log-file -
worker: python manage.py celery worker --loglevel=info