#!/bin/bash
cd app
python manage.py makemigrations user
python manage.py makemigrations image
python manage.py makemigrations post

python manage.py migrate 
echo "Django is ready.";
python manage.py runserver 0.0.0.0:8000