web: gunicorn smartcms.wsgi:application --log-file - --workers 3
release: python manage.py migrate --noinput
