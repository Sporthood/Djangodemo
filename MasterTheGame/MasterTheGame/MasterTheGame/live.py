import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://propicks.qburst.com/backend'
SITE_URL = 'http://propicks.qburst.com/'
#URL_PREFIX = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'propicks',
        'USER': 'upropicks',
        'PASSWORD': 'propicks@45%',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
