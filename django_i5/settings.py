"""
Base Django settings for web applications running behind i5
Copyright (c) 2020 Nathan Osman
"""

import email.utils
import os
import socket
import sys


def find_settings():
    """
    Find the absolute path to the Django settings module

    Many of the paths used in this file are resolved relative to the settings
    module (specified in the DJANGO_SETTINGS_MODULE environment variable).
    Python's import machinery is used to determine the absolute path to this
    file, since importing it would result in a cyclical import.
    """
    module_name = os.environ['DJANGO_SETTINGS_MODULE']
    for finder in sys.meta_path:
        spec = finder.find_spec(module_name, None)
        if spec is not None:
            break
    else:
        raise ModuleNotFoundError(
            "Unable to find the module {}".format(module_name),
        )
    return os.path.abspath(spec.origin)


# Determine the path to the project's root directory
BASE_DIR = os.path.dirname(os.path.dirname(find_settings()))

# Determine the site name and domain
SITE_NAME = os.environ['SITE_NAME']
SITE_DOMAIN = os.environ['SITE_DOMAIN']


#################
# Core settings #
#################

DEBUG = 'DEBUG' in os.environ
SECRET_KEY = os.environ.get('SECRET_KEY', 'DEBUG' if DEBUG else '')

ALLOWED_HOSTS = ['*'] if DEBUG else [SITE_DOMAIN]

USE_X_FORWARDED_HOST = True

USE_TZ = True
TIME_ZONE = 'UTC'


#####################
# Database settings #
#####################

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': os.environ.get('DB_HOST', 'postgres'),
            'NAME': os.environ.get('DB_NAME', socket.gethostname()),
            'USER': os.environ.get('DB_USER', socket.gethostname()),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        }
    }


##################
# Email settings #
##################

ADMINS = email.utils.getaddresses([os.environ.get('ADMINS', '')])

DEFAULT_FROM_EMAIL = SERVER_EMAIL = \
    "{} <donotreply@{}>".format(SITE_NAME, SITE_DOMAIN)

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'pyhectane.django.HectaneBackend'

HECTANE_HOST = os.environ.get('HECTANE_HOST', 'hectane')


#####################
# Template settings #
#####################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, "jinja2"),
        ],
    },
]


#########################
# Static files settings #
#########################

STATIC_ROOT = '/srv/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


########################
# Media files settings #
########################

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') if DEBUG else '/srv/media/'
MEDIA_URL = '/media/'


# Build the list of symbols exported by this module
__all__ = (
    'DEBUG',
    'SECRET_KEY',
    'ALLOWED_HOSTS',
    'USE_X_FORWARDED_HOST',
    'USE_TZ',
    'TIME_ZONE',

    'DATABASES',

    'ADMINS',
    'DEFAULT_FROM_EMAIL',
    'SERVER_EMAIL',
    'EMAIL_BACKEND',
    'HECTANE_HOST',

    'TEMPLATES',

    'STATIC_ROOT',
    'STATIC_URL',
    'STATICFILES_DIRS',

    'MEDIA_ROOT',
    'MEDIA_URL',
)
