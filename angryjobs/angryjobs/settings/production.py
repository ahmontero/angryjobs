"""Development settings and globals."""


from os import environ

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INSTALLED_APPS += (
    'debug_toolbar',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
########## END TOOLBAR CONFIGURATION


########## django-twitter CONFIGURATION
GLOBAL_PWD = environ.get('TE_GLOBAL_PWD', '')

LOGIN_REDIRECT_URL = 'http://domain.com'
LOGIN_URL = 'http://domain.com/twitter/login/'
CALLBACK_URL = 'http://domain.com'

AUTH_PROFILE_MODULE = 'web.UserProfile'

CONSUMER_KEY = environ.get('TE_CONSUMER_KEY', '')
CONSUMER_SECRET = environ.get('TE_CONSUMER_SECRET', '')
########## END django-twitter CONFIGURATION


########## API CONFIGURATION
API_USER = environ.get('TE_API_USER', '')
API_KEY = environ.get('TE_API_KEY', '')
########## END API CONFIGURATION

########## captcha CONFIGURATION
CAPTCHA_PUBLIC_KEY = environ.get('TE_CAPTCHA_PUBLIC_KEY', '')
CAPTCHA_PRIVATE_KEY = environ.get('TE_CAPTCHA_PRIVATE_KEY', '')
########## END captcha CONFIGURATION
