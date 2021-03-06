"""
Django settings for mowimu_backend project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os, sys
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PyInstaller working dir and EXE location
pyinstaller_exe_path = ''
pyinstaller_exe_dir = ''
if getattr(sys, 'frozen', False):
    # Running in a PyInstaller bundle, look for the DB file in the same dir as the EXE
    pyinstaller_exe_path = sys.executable
    pyinstaller_exe_dir = os.path.dirname(os.path.realpath(pyinstaller_exe_path))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '362y+*33)8)%5)$c&_%&-guosnh%eo_!g7%s59^v7@aee51!)y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# LOGGING configuration is in util/bootstrap.py

# Application definition

INSTALLED_APPS = [
    'mowimu_inventory.apps.MowimoInventoryConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mowimu_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mowimu_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if getattr(sys, 'frozen', False) :
    # Running in a PyInstaller bundle, look for the DB file in the same dir as the EXE
    db_path = os.path.join(pyinstaller_exe_dir, 'db.sqlite3')
else :
    # Running 'manage.py' directly in development mode
    db_path = os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_path,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

# Static files are inside the PyInstaller bundle, so BASE_DIR points to the correct location
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'

if getattr(sys, 'frozen', False) :
    # Running in a PyInstaller bundle, save media in the same dir as the EXE
    media_path = os.path.join(pyinstaller_exe_dir, 'media')
else :
    # Running 'manage.py' directly in development mode
    media_path = os.path.join(BASE_DIR, 'media')

# BASE_DIR is the directory that contains manage.py
MEDIA_ROOT = media_path