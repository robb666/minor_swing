#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py migrate
python manage.py collectstatic --noinput
