"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
CDN_HOST = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
ALLOWED_HOSTS = ['https://maren-photo.herokuapp.com/', CDN_HOST, 'localhost',]

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'blog',
    'imagekit',
    'django_filters',
    'storages',
    #'compressor', Removed due to incompatibility with whitenoise.

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    #'compression_middleware.middleware.CompressionMiddleware', #Incompatible with whitenoise, Debug=False.
    # Use CDN or whitenoise compression instead
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Activate Django-Heroku.
django_heroku.settings(locals())

# Static files (CSS, JavaScript, Images)

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

#CDN Variables
STATIC_DISTRIBUTION_ID = os.environ.get('STATIC_DISTRIBUTION_ID')
AWS_S3_CDN_DOMAIN = '{}.cloudfront.net'.format(STATIC_DISTRIBUTION_ID)

#Amazon S3 Variables
AWS_ACCESS_KEY_ID =  os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=31536000',
    'Expires': 'Thu, 31 Dec 2031 20:00:00 GMT',
}

AWS_LOCATION = 'static/'
STATIC_HOST = AWS_S3_CUSTOM_DOMAIN if not DEBUG else ''
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = 'https://%s/media/'.format(AWS_S3_CUSTOM_DOMAIN)
MEDIA_LOCATION = 'media/'
MEDIA_ROOT = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, MEDIA_LOCATION)

AWS_DEFAULT_ACL = "public-read"
AWS_S3_REGION_NAME='eu-north-1'

#For faster performance - AWS headers
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2031 20:00:00 GMT',
    'Cache-Control': 'max-age=31536000',
}

#Email backend
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_REGION_NAME= 'eu-north-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-north-1.amazonaws.com'

#Logging for DEBUG=FALSE - DEBUG.log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}