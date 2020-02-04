#!/bin/bash

python manage.py makemigrations accounts
python manage.py makemigrations images
python manage.py makemigrations posts

python manage.py migrate 

echo "Django is ready!!!";
#python manage.py runserver 0.0.0.0:8000
uwsgi --http :8000 --wsgi-file dailypicture/wsgi.py
