"""
Django settings for organisation_app project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import sys

if os.path.exists("env.py"):
    import env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CLOUDINARY_STORAGE = {"CLOUDINARY_URL": os.environ.get("CLOUDINARY_URL")}
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "DEV" in os.environ

ALLOWED_HOSTS = [
    os.environ.get("ALLOWED_HOST"),
    "localhost",
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "django.contrib.staticfiles",
    "cloudinary",
    "rest_framework",
    "django_filters",
    "rest_framework.authtoken",
    "dj_rest_auth",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    'corsheaders',
    "app_profile",
    "app_event",
    "app_post",
    "app_comment",
    "app_like",
    "app_follower",
    "app_memory",
    "app_calendar",
    "app_watch",
]
SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    os.environ.get('CLIENT_ORIGIN'),
]

CSRF_TRUSTED_ORIGINS = [
    os.environ.get('CLIENT_ORIGIN'),
]

ROOT_URLCONF = "organisation_app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "organisation_app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if os.getenv("GITHUB_WORKFLOW"):
    # check if in GITHUB ACTION MODE
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "github-actions",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "localhost",
            "PORT": "5432",
        }
    }
else:
    # check if unittest running locally
    if "test" in sys.argv[0] or "test" in sys.argv[1]:
        DATABASES = {
            "default": {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
    else:
        DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": [
        (
            "rest_framework.authentication.SessionAuthentication"
            if "test" in sys.argv[0] or "test" in sys.argv[1]
            else "dj_rest_auth.jwt_auth.JWTCookieAuthentication"
        )
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DATETIME_FORMAT": "%d %b %Y",
}


REST_USE_JWT = True  # enables JWT token usage
JWT_AUTH_SECURE = True  # ensures tokens send over HTTPS only
JWT_AUTH_COOKIE = "my-app-auth"  # access token
JWT_AUTH_REFRESH_COOKIE = "my-refresh-token"  # refresh token
JWT_AUTH_SAMESITE = 'None'

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "organisation_app.serializers.CurrentUserSerializer"
}

if "DEV" not in os.environ:
    REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [
        "rest_framework.renderers.JSONRenderer",
    ]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ACCOUNT_EMAIL_VERIFICATION = 'none'