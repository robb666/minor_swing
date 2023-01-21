from storages.backends.s3boto3 import S3StaticStorage
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3StaticStorage):
    location = settings.AWS_STATIC_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    file_overwrite = True


# StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
# MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='media')
