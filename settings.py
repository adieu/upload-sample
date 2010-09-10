try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

import os

# Uncomment the following if you want to use MongoDB
# -----------------
#DATABASES = {
#    'default': {
#        'ENGINE': 'django_mongodb_engine.mongodb',
#        'NAME': 'test',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': 'localhost',
#        'PORT': 27017,
#        'SUPPORTS_TRANSACTIONS': False,
#    }
#}
#
#DEFAULT_FILE_STORAGE = 'storages.backends.mongodb.GridFSStorage'
#GRIDFS_DATABASE = 'default'
# -----------------

# Use this if you have a base URL for public downloads
#PUBLIC_DOWNLOAD_URL_BACKEND = 'filetransfers.backends.base_url.public_download_url'
#PUBLIC_DOWNLOADS_BASE_URL = '/gridfs/'

INSTALLED_APPS = (
    'djangotoolbox',
#    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'upload',
    'filetransfers',
)

USE_I18N = False

if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

ADMIN_MEDIA_PREFIX = '/media/admin/'
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

# Activate django-dbindexer if available
try:
    import dbindexer
    DATABASES['native'] = DATABASES['default']
    DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
    INSTALLED_APPS += ('dbindexer',)
except ImportError:
    pass
