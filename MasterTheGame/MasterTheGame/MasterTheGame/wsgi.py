"""
WSGI config for MasterTheGame project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""


import os, sys, site

VIRTUAL_ENV_PATH = ['/home/sanooj/Documents/Projects/env/lib/python2.7/site-packages']


prev_sys_path = list(sys.path)
# Add each new site-packages directory.
for directory in VIRTUAL_ENV_PATH:
  site.addsitedir(directory)

# Reorder sys.path so new directories at the front.
new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path


path = '/home/sanooj/Documents/Projects/sportz4you/MasterTheGame/MasterTheGame'


if path not in sys.path:
    sys.path.append(path)



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MasterTheGame.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
