import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://10.1.3.114:8080/backend'
SITE_URL = 'http://10.1.3.114:8080/'


#URL_PREFIX = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'MasterTheGame',
        'USER': 'postgres',
        'PASSWORD': 'newPassword',
        'HOST': 'LOCALHOST',
        'PORT': '5432',
    }
}
