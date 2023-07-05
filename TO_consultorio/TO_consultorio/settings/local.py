from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'consultorio',
        'USER': 'postgres',
        'PASSWORD': 'Alejandro',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}



