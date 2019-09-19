# -*- coding: utf-8 -*-

"""
Django settings for artemis project.

Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import os
import platform
from Queue import Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f*^r_l#@o%+aaa0=5$pu=g(xn=)q$)al3$a18zam4sai8985xj'

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = 'authority.UserInfo'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authority',
    'projects',
    'repertory',
    'mail_templated',
    'djcelery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authority.middleware.authentication.ValidPermission',
]

ROOT_URLCONF = 'artemis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'artemis.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Logging Path by different OS(windows|Linux etc)
if 'window'.lower() in platform.system().lower():
    LOG_PATH = BASE_DIR + os.sep + 'logs'
else:
    LOG_PATH = BASE_DIR + os.sep + "logs"

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'INFO',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'sys.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'sys.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_PATH, 'script.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'deploy.app': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'scripts': {
            'handlers': ['scprits_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# Email
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 25
EMAIL_SSL_PORT = 465
EMAIL_HOST_USER = 'noc@example.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_FROM_USER = 'noc@example.com'
RECEIVE_USERS = 'ops@example.com'

# artifacts
if 'window'.lower() in platform.system().lower():
    ARTIFACTS_DIR = 'D:/jenkins/artifacts'
    MOUNT_POINT_PREFIX = 'D:/jenkins/artifacts'
    ZIP_BASE_DIR = 'D:/tem/zip/'
    UNZIP_BASE_DIR = 'D:/tem/unzip/'
else:
    ARTIFACTS_DIR = '/home/jenkins/artifacts'
    MOUNT_POINT_PREFIX = '/home/jenkins/artifacts'
    ZIP_BASE_DIR = '/home/tmp/zip/'
    UNZIP_BASE_DIR = '/home/tmp/unzip/'
if not os.path.exists(ARTIFACTS_DIR):
    os.makedirs(ARTIFACTS_DIR)

# log

if 'window'.lower() in platform.system().lower():
    PUSH_LOG_LOCAL_DIR_PREFIX = 'd:/logs'
else:
    PUSH_LOG_LOCAL_DIR_PREFIX = '/usr/local/src/logs'

if not os.path.exists(PUSH_LOG_LOCAL_DIR_PREFIX):
    os.makedirs(PUSH_LOG_LOCAL_DIR_PREFIX)

if not os.path.exists(ZIP_BASE_DIR):
    os.makedirs(ZIP_BASE_DIR)

if not os.path.exists(UNZIP_BASE_DIR):
    os.makedirs(UNZIP_BASE_DIR)

# file upload
MEDIA_URL = '/upload/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')

# download stable version local tmp path
if 'window'.lower() in platform.system().lower():
    COPY_STABLE_LOCAL_TMP_PATH = 'd:/tmp'
else:
    COPY_STABLE_LOCAL_TMP_PATH = '/usr/local/src/local_tmp_path'

if not os.path.exists(COPY_STABLE_LOCAL_TMP_PATH):
    os.makedirs(COPY_STABLE_LOCAL_TMP_PATH)

# DEPLOY_Q
DEPLOY_Q = Queue()