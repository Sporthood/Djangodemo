import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://www.sportz4you.org/'
SITE_URL = 'http://www.sportz4you.org/'
#URL_PREFIX = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sport',
        'USER': 'postgres',
	'PASSWORD':'masterthegame',
        'HOST': 'LOCALHOST',
        'PORT': '5432',
    }
}
