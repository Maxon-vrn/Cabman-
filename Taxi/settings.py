"""
Django settings for Taxi project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# говорит о шифровании
SECRET_KEY = 'django-insecure-e2$3zldg!p5*_aqr-q9f0v_usp*2f18kv1!frtw-2kryfor$tl'

# SECURITY WARNING: don't run with debug turned on in production!
# информация о ошибках: нужно для отображения в режими отладки проблем и ошибок 
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition
# указываются для включения прилоения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth', # auntification on sait register user
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "debug_toolbar",
    'post.apps.PostConfig', # - добавляем свою страницу post /приложение/пакет для проекта Такси
    'captcha',      # verification on bot or people
    'analytical'    # django packe to yandex analitica,see wore information on dockumentation
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # auntification on sait register user
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]
# место нахождение главного файла
ROOT_URLCONF = 'Taxi.urls'

# говорит о том где находятся наши шаблоны и html файлы
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  #определение собственного пути к своей странице администратора
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ #то что выполняется на абсолютно на всем сайте
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# подключение файла wsgi
WSGI_APPLICATION = 'Taxi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
# подключение к базе данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'
# нужно ли переводить весь сайт
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIR = [] #STATICFILES_DIR = [os.path.join(BASE_DIR,'static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR,'media') #формируем путь к каталогу с фотографиями;BASE_DIR-корень каталога и папка которую ищем
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    # debug_toolbar see more information on documentation
    "127.0.0.1",
    
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cabman_cache'),
        'OPTIONS': {
            'MAX_ENTRIES': 1000 #максимальное количество записей в кеш
        }
    }   
}

#This bloc is settings to capcha on page cabman
#CAPTCHA_IMAGE_SIZE=[150,60]
#CAPTCHA_FONT_SIZE=30

# metrica - django-analitica - dockumentation on settings
YANDEX_METRICA_COUNTER_ID = '12345678'
YANDEX_METRICA_WEBVISOR=True
YANDEX_METRICA_TRACKHASH=True
YANDEX_METRICA_NOINDEX=True
YANDEX_METRICA_ECOMMERCE=True
ANALYTICAL_INTERNAL_IPS = ['192.168.1.45', '192.168.1.57'] # указываем какие не отслеживать ip адреса, если убрать пункт, будет отслеживать все кроме локального хоста