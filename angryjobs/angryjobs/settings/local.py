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

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': False,
    'TAG': 'div',
    'ENABLE_STACKTRACES': True
}
########## END TOOLBAR CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'
########## END PROFILE CONFIGURATION


########## DJANGO-TWITTER CONFIGURATION
GLOBAL_PWD = environ.get('TE_GLOBAL_PWD', '')

LOGIN_REDIRECT_URL = 'http://127.0.0.1:8000'
LOGIN_URL = 'http://127.0.0.1:8000/twitter/login/'
CALLBACK_URL = 'http://127.0.0.1:8000'

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
