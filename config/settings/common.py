from os import environ
from pathlib import Path
from datetime import timedelta



# GET ENV UTIL
def get_env(key, default=None, optinal=False):
    """Return environment variables with some options."""
    val = environ.get(key)
    if val is not None:
        return val
    elif default is not None:
        return default
    elif not optinal:
        raise ValueError(f"Environment variable {key} was not defined")
# END GET ENV UTIL


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SITE_ID = 2

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


# APP CONFIGURATION
DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",
)

THIRD_PARTY_APPS = (
    "rest_framework",
    "django_filters",
    "corsheaders",
    "gunicorn",
    "django.contrib.sites",
    "drf_social_oauth2",
    "oauth2_provider",
)

# Apps specific for this project go here.

LOCAL_APPS = (
    "accounts",
    "podcast",
    "feeling",
    "emotion",
    "reminder",
    "behavior",
    "AIrefer",
    "report",
    "journey",
    "analyze",
)


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
# END APP CONFIGURATION

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    #"allauth.account.middleware.AccountMiddleware",
    #"utilities.middlware.CrossDomainSessionMiddleware",
]

ROOT_URLCONF = "config.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates/",
        ],
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

WSGI_APPLICATION = "config.wsgi.application"


#ACCOUNT_EMAIL_VERIFICATION = "none"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nnnn@nn.com' #sender's email-id
EMAIL_HOST_PASSWORD = 'nnn22222aaaam' #password associated with above email-id



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = get_env("STATIC_ROOT", default="/static/")
STATIC_URL = get_env("STATIC_URL", default="/static/")
MEDIA_ROOT =BASE_DIR/"media"
MEDIA_URL = get_env("MEDIA_URL", default="/media/")
static_file_env = get_env("STATICFILES_DIRS", optinal=True)

STATICFILES_DIRS = (
    static_file_env.split(",") if static_file_env is not None else ["docs/"]
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

'''
# CACHING CONFIGURATION
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://5.161.144.222:6379/1",
    }
}
# END CACHING CONFIGURATION
'''

# AUTH USER MODEL CONFIGURATION
AUTH_USER_MODEL = "accounts.User"
# END AUTH USER MODEL CONFIGURATION

# OTP CONFIGURATION
OTP_CODE_LENGTH = int(get_env("OTP_CODE_LENGTH", default="4"))
OTP_TTL = int(get_env("OTP_TTL", default="120"))
# END OTP CONFIGURATION



# JWT SETIINGS
ACCESS_TTL = int(get_env("ACCESS_TTL", default="3"))  # days
REFRESH_TTL = int(get_env("REFRESH_TTL", default="12"))  # days

#ACCESS_TTL = 10000#0.0006
#REFRESH_TTL = 10000#0.005

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=4320),  # Set your desired access token lifetime
    'REFRESH_TOKEN_LIFETIME': timedelta(days=12),    # Set your desired refresh token lifetime
}

'''
ACCESS_TIME = timedelta(minutes=10)
ACCESS_TTL = int(ACCESS_TIME.total_seconds() / 60 )
print(ACCESS_TTL)

REFRESH_TIME = timedelta(minutes=15)
REFRESH_TTL = int(REFRESH_TIME.total_seconds() / 60 )
print(REFRESH_TTL)
'''
# END JWT SETTINGS



# Google Configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "366111965494-bbgflimp8s9dtndoufsah3v235bt8lhh.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"

# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]



# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "accounts.backends.JWTAuthentication",
        #'allauth.account.auth_backends.AuthenticationBackend',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    "DEFAULT_THROTTLE_RATES": {"otp": get_env("OTP_THROTTLE_RATE", default="10/min"), },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# END REST FRAMEWORK CONFIGURATION

MAX_UPLOAD_SIZE = 5242880

# CORSHEADERS CONFIGURATION
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '5.161.144.222', 'helpfinity.btrr.me', 'btrr.me']

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://5.161.144.222",
    "http://btrr.me"
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://127.0.0.1",
    "http://5.161.144.222",
    "http://btrr.me"
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
APPEND_SLASH = True

