#!/bin/sh

set -e

python manage.py collectstatic --no-input -v 0
python manage.py migrate
