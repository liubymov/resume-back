#!/usr/bin/env bash

pip install -r /usr/src/resume/requirements.txt
python /usr/src/resume/manage.py migrate
python /usr/src/resume/manage.py collectstatic --noinput
exec python /usr/src/resume/manage.py runserver 0.0.0.0 8000
