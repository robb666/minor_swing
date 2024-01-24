from storages.backends.s3boto3 import S3StaticStorage
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticStorage(S3StaticStorage):
    location = settings.AWS_STATIC_LOCATION

    # def __init__(self, *args, **kwargs):
    #     kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
    #     super(StaticStorage, self).__init__(*args, **kwargs)

class MediaStorage(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    file_overwrite = True

    # def __init__(self, *args, **kwargs):
    #     kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
    #     super(MediaStorage, self).__init__(*args, **kwargs)


# StaticRootS3BotoStorage = lambda: S3Boto3Storage(location='static')
# MediaRootS3BotoStorage = lambda: S3Boto3Storage(location='media')
