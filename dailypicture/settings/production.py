from .base import *

iDEBUG = False

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


# S3 storage
DEFAULT_FILE_STORAGE = 'dailypicture.settings.storages.MediaStorage'
#STATICFILES_STORAGE = 'dailypicture.settings.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
#STATICFILES_LOCATION = 'static'

# AWS Access
AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'