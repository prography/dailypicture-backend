from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
import os
from tempfile import SpooledTemporaryFile


class CustomS3Boto3Storage(S3Boto3Storage):
    def _save_content(self, obj, content, parameters):
        content.seek(0, os.SEEK_SET)
        content_autoclose = SpooledTemporaryFile()
        content_autoclose.write(content.read())
        super(CustomS3Boto3Storage, self)._save_content(
            obj, content_autoclose, parameters
        )
        if not content_autoclose.closed:
            content_autoclose.close()


class MediaStorage(CustomS3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION


# class StaticStorage(S3Boto3Storage):
#    location = settings.STATICFILES_LOCATION
