from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG').lower() == 'true'
SERVER_HOST = "https://islombek.alwaysdata.net"
# SERVER_HOST = env('CURRENT_PROTOCOL') + '://' + env(
#     'CURRENT_HOST') + f"{':' + env('CURRENT_PORT') if len(env('CURRENT_PORT')) else ''}"

ALLOWED_HOSTS = ["islombek.alwaysdata.net", "127.0.0.1", "localhost"]


# Application definition

INTERNAL_APPS = [
    "core_admin",
    "davomat",
    "groups",
    "payment",
    "student",
    "teacher"
]

INSTALLED_APPS = (
    [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ] + INTERNAL_APPS
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'core_admin.User'


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

POSTGRES_DB_CONF = {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': env('DATABASE_NAME', default='test_project_db'),
    'USER': env('DATABASE_USER', default='postgres'),
    'PASSWORD': env('DATABASE_PASSWORD', default='1'),
    'HOST': env('DATABASE_HOST', default='localhost'),
    'PORT': env('DATABASE_PORT', default='5432'),
    'OPTIONS': {
            'options': '-c search_path=django_admin,public'
    }
}

SQLITE_DB_CONF = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

DATABASES = {
    'default': POSTGRES_DB_CONF,

} 


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'
TIME_FORMAT = '%m/%d/%Y %H:%M'
DATETIME_FORMAT = '%m/%d/%Y %H:%M'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    "https://islombek.alwaysdata.net"
    'http://localhost:8000',
    'http://127.0.0.1:8000',
]