#!/bin/bash
cd backend
python3 manage.py migrate --noinput || exit 1
python3 manage.py createsuperuser --noinput
python3 manage.py runserver 0.0.0.0:8000
exec "$@"
