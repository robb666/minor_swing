#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

#DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email #$SUPER_USER_EMAIL --noinput

gunicorn frukt.wsgi:application --bind ec2-16-171-20-189.eu-north-1.compute.amazonaws.com:8080
