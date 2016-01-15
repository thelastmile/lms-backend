"""
Django settings for lmsbackend project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z+@$j&p-vl4b%npl)1!1^^pfymp#&ehmc-*5=nq&9ar!)cwq0f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'lms_backend_app',
    'rest_framework_swagger',
    'rest_framework.authtoken',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'lmsbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lmsbackend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# RDS is for elastic beanstalk / ec2
# If anything else just use/create sqlite localdb in the current path
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# CORS_ALLOW_HEADERS = (
#  'x-requested-with',
#  'content-type',
#  'accept',
#  'origin',
#  'authorization',
#  'X-CSRFToken',
#  'Api-Authorization',
# )

# CORS_ALLOW_METHODS = (
#  'GET',
#  'POST',
#  'PUT',
#  'PATCH',
#  'DELETE',
#  'OPTIONS'
# )

# DRF Settings
# disabled auth for easier testing.
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.SessionAuthentication',),
}

#REST_FRAMEWORK = {
#    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
#    'DEFAULT_AUTHENTICATION_CLASSES': (
#        'rest_framework.permissions.AllowAny',
#        #'oauth2_provider.ext.rest_framework.OAuth2Authentication',
#        #'rest_framework.authentication.TokenAuthentication',
#    ),
#    'DEFAULT_PERMISSION_CLASSES': (
#        'rest_framework.permissions.IsAuthenticated',
#    )
#}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# AMAZON S3
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'lms-backend-static-dev'

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATIC_URL = "//%s.s3.amazonaws.com/" % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = '%sgrappelli/' % STATIC_URL

MEDIA_URL = "//s3.amazonaws.com/%s/" % AWS_STORAGE_BUCKET_NAME
#STATIC_DIRECTORY = '/static/'
MEDIA_DIRECTORY = '/media/'

# LOCAL FILESYSTEM (DISABLED)
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
# DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# STATIC_DIRECTORY = '/var/tlm-lms/static/'
# STATIC_URL = '/static/'

# MEDIA_ROOT = '/var/tlm-lms/media/' # Absolute path to local file system (or network path) with trailing slash
# MEDIA_URL = '/media/'

# File upload perms
FILE_UPLOAD_PERMISSIONS = 0555
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0555
FILE_UPLOAD_TEMP_DIR = '/tmp' # Docs show no trailing slash?  Silly Django
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600 #100MB

# FILE PATHS, RELATIVE TO MEDIA_ROOT, With trailing slash only
# These directories will be created if they don't exist
MEDIA_IMG = 'img/'
MEDIA_VIDEO = 'video/'
MEDIA_PDF = 'pdf/'
MEDIA_HTML ='html/'
MEDIA_DOCS = 'docs/'
MEDIA_MISC = 'misc/'
MEDIA_PHOTOS = 'photos/'
MEDIA_CONTENT_THUMBNAILS = 'content_thumbnails/'

# Import local settings
try:
    from local_settings import *
except ImportError:
    pass

# Make directories AFTER loading local_settings

# Create our file directories
# directory = '%s' % (MEDIA_ROOT)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_IMG)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_VIDEO)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_PDF)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_HTML)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_DOCS)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_MISC)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_PHOTOS)
# if not os.path.exists(directory):
#     os.makedirs(directory)
# directory = '%s%s' % (MEDIA_ROOT,MEDIA_CONTENT_THUMBNAILS)
# if not os.path.exists(directory):
#     os.makedirs(directory)