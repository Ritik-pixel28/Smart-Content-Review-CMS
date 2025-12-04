release: python manage.py migrate --noinput && python manage.py collectstatic --noinput
web: gunicorn smartcms.wsgi:application --log-file - --workers 3 --bind 0.0.0.0:$PORT
