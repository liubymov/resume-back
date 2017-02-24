#!/usr/bin/env bash

set -x
set -e

pip install -r /usr/src/resume/requirements.txt
python /usr/src/resume/manage.py migrate
python /usr/src/resume/manage.py collectstatic --noinput

cat <<EOF | python manage.py shell
from django.contrib.auth.models import User
User.objects.filter(username="admin").exists() or \
    User.objects.create_superuser("admin", "admin@example.com", "admin")
EOF

exec python /usr/src/resume/manage.py runserver 0.0.0.0:8000
