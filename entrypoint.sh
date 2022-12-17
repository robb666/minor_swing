#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn frukt.wsgi:application --bind 0.0.0.0:8080 --timeout 0
