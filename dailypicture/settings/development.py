from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*', ]


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secret("DJANGO_DB_NAME"),
        'USER': get_secret("DJANGO_DB_USERNAME"),
        'PASSWORD': get_secret("DJANGO_DB_PASSWORD"),
        'HOST': get_secret("DJANGO_DB_HOST"),
        'PORT': get_secret("DJANGO_DB_PORT"),
    }
}
