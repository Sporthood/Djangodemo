import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://127.0.0.1:8000/backend'
SITE_URL = 'http://127.0.0.1:8000/'


#URL_PREFIX = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'developer',
        'USER': 'postgres',
        'PASSWORD': 'dfDDrbj7',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
