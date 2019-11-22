from .base import *

DEBUG = False

ALLOWED_HOSTS = ['dailypicture-cname.ap-northeast-2.elasticbeanstalk.com']


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DJANGO_DB_NAME"),
        'USER': get_secret("DJANGO_DB_USERNAME_PRODUCTION"),
        'PASSWORD': get_secret("DJANGO_DB_PASSWORD"),
        'HOST': get_secret("DJANGO_DB_HOST_PRODUCTION"),
        'PORT': get_secret("DJANGO_DB_PORT"),
    }
}