from django.contrib.messages import constants as messages
"""
Django settings for cloudsmart project.

Generated by 'django-admin startproject' using Django 2.0.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fv3+-^+b+jy$54#2p%z8+(w@84w*mcv%i@qb#eo6z%*3g65$^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Orig
# DEBUG = True ## For TESTING only - BWC

#ALLOWED_HOSTS = ['apps.cloudsmartgis.com', 'localhost']
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'apps.apps.AppsConfig',
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',
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

ROOT_URLCONF = 'cloudsmart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cloudsmart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cloudsmart',
        'USER': 'postgres',
        'PASSWORD': 'Bialy$tok821',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

#STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'cloudsmart', 'static'))
#STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_URL = '/cloudsmart-jump-page/static/'
STATIC_URL = '/cloudsmart/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'cloudsmart/static')
]

# Media Folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL = '/cloudsmart-jump-page/media/'
MEDIA_URL = '/cloudsmart/media/'


# Messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'cloudsmartgis@gmail.com'  # os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = '$martGIS16'  # os.environ.get('EMAIL_PASS')
