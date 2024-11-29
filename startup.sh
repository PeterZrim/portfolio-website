#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start Gunicorn
gunicorn portfolio_website.wsgi:application --bind=0.0.0.0:8000
