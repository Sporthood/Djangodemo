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
        'NAME': 'MasterTheGame',
        'USER': 'masterthegame',
        'PASSWORD': 'sportsforyou',
        'HOST': 'master.cfjahnp3vgzx.us-west-2.rds.amazonaws.com:5432',
        'PORT': '5432',
    }
}
