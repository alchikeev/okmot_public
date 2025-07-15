import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Международные настройки (Internationalization) ---
# Устанавливаем язык по умолчанию на русский.
# Этот язык будет использоваться, если пользователь явно не выбрал другой или его браузер не предоставил предпочтений.
LANGUAGE_CODE = 'ru'

# Определяем список всех поддерживаемых языков на вашем сайте.
# Django будет искать переводы для этих языков.
LANGUAGES = [
    ('ru', _('Русский')),
    ('kg', _('Кыргызча')),
]

# Указываем Django, где искать файлы переводов (.po, .mo).
# Мы добавляем папку 'locale' в корневую директорию проекта.
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Включаем систему интернационализации Django.
USE_I18N = True

# --- Общие настройки Django ---
SECRET_KEY = 'django-insecure-4@6hiu0bxd&!&^j=kz5m=ixct1v%zkij#z0moo!e75*0thi9(*'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.main',
    'apps.news',
    'apps.documents',
    'apps.appeals',
    'apps.about',
    'apps.council',
    'apps.investors',
    'apps.community',
    'apps.gallery',
    'apps.info',
    'apps.search',
]


# Важное изменение: LocaleMiddleware должен быть после SessionMiddleware и CommonMiddleware,
# но до CsrfViewMiddleware. Это обеспечивает правильное определение языка перед обработкой запроса.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware', # CommonMiddleware должен быть перед LocaleMiddleware
    'django.middleware.locale.LocaleMiddleware', # LocaleMiddleware здесь
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

TIME_ZONE = 'Asia/Bishkek' # Установил часовой пояс для Кыргызстана
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Настройки для медиа-файлов (изображений, документов)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'