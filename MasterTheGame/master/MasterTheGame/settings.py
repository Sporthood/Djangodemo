"""
Django settings for MasterTheGame project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from local import *
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l1iu*ww!_vtm6tildjru)tq)i*a!@gt=m62^4n!04f(qrkqyn+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587
EMAIL_HOST_USER = 'rockingmammoottyfans@gmail.com'
EMAIL_HOST_PASSWORD = 'mammootty222'
DEFAULT_FROM_EMAIL = 'rockingmammoottyfans@gmail.com'


STATIC_URL = BASE_URL+'/static/'
MEDIA_URL = BASE_URL+'/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, '/static')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


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



ROOT_URLCONF = 'MasterTheGame.urls'

WSGI_APPLICATION = 'MasterTheGame.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
CORS_ORIGIN_ALLOW_ALL = True  # Default False
CORS_ORIGIN_WHITELIST = (
       'localhost:8101/',
       'http://ec2-52-37-207-235.us-west-2.compute.amazonaws.com/',
           )
# CORS_ORIGIN_REGEX_WHITELIST = ('^http?://(\w+\.)?google\.com$', )
CORS_ALLOW_METHODS = (
       'GET',
       'POST',
       'PUT',
       'PATCH',
       'DELETE',
       'OPTIONS'
   )
CORS_ALLOW_HEADERS = (
       'x-requested-with',
       'content-type',
       'accept',
       'origin',
        'authorization',
        'X-CSRFToken',
        'session-key',
        'page',
    )
# CORS_EXPOSE_HEADERS = ()
# CORS_PREFLIGHT_MAX_AGE = 86400
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = True
