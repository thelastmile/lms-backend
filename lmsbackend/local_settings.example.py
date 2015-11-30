import os
SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__))

email_host_user = ''
email_host = ''
email_port = 587
email_use_tls = True
email_host_password = ''
DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = '%s/media/' % SETTINGS_PATH
FILE_UPLOAD_PERMISSIONS = 0777
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0777