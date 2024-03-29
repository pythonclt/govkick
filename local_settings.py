import os.path
import django.conf.global_settings as DEFAULT_SETTINGS

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.split(PROJECT_DIR)[0]


STATIC_ROOT = ''
STATIC_URL = '/static/'
MEDIA_ROOT = ROOT_DIR + '/media/'
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'
ADMIN_MEDIA_PREFIX = '/media/admin/'
CACHES = {}

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ADMINS = ()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'govkick_development',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
