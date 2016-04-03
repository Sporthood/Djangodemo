import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_URL = 'http://ec2-52-37-207-235.us-west-2.compute.amazonaws.com/'
SITE_URL = 'http://ec2-52-37-207-235.us-west-2.compute.amazonaws.com/'
#URL_PREFIX = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'MasterTheGame',
        'USER': 'MasterTheGame',
        'PASSWORD': 'MasterTheGame',
        'HOST': 's4u.cfjahnp3vgzx.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
