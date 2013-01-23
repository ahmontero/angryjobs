"""Development settings and globals."""


from os import environ

from base import *



########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': normpath(join(DJANGO_ROOT, 'angryjobs.db')),
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


########## django-twitter CONFIGURATION
GLOBAL_PWD = environ.get('TE_GLOBAL_PWD', '')

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000'
LOGIN_URL = 'http://127.0.0.1:8000/twitter/login/'
CALLBACK_URL = 'http://127.0.0.1:8000'

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
