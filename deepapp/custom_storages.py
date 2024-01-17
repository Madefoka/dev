# custom_storages.py

from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    location = 'media'  # Set the desired folder name within the S3 bucket for media files
    file_overwrite = False  # Optional: Set to True if you want to overwrite files with the same name
