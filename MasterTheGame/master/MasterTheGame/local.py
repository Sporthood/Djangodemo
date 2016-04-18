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
        'NAME': 'Master',
        'USER': 'postgres',
        'PASSWORD': 'newPassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
