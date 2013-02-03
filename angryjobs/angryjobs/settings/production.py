"""Development settings and globals."""


from os import environ

import dj_database_url

from base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {}

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## DJANGO-TWITTER CONFIGURATION
GLOBAL_PWD = environ.get('TE_GLOBAL_PWD', '')

LOGIN_REDIRECT_URL = 'http://domain.com'
LOGIN_URL = 'http://domain.com/twitter/login/'
CALLBACK_URL = 'http://domain.com'

AUTH_PROFILE_MODULE = 'web.UserProfile'

CONSUMER_KEY = environ.get('TE_CONSUMER_KEY', '')
CONSUMER_SECRET = environ.get('TE_CONSUMER_SECRET', '')
########## END DJANGO-TWITTER CONFIGURATION


########## API CONFIGURATION
API_USER = environ.get('TE_API_USER', '')
API_KEY = environ.get('TE_API_KEY', '')
########## END API CONFIGURATION

########## CAPTCHA CONFIGURATION
CAPTCHA_PUBLIC_KEY = environ.get('TE_CAPTCHA_PUBLIC_KEY', '')
CAPTCHA_PRIVATE_KEY = environ.get('TE_CAPTCHA_PRIVATE_KEY', '')
########## END CAPTCHA CONFIGURATION
