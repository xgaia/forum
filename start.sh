#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python manage.py migrate
gunicorn makinaforum.wsgi --bind 0.0.0.0:8000 --chdir=/forum --timeout 360
