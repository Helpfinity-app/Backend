from pathlib import Path
from urllib.parse import quote
from dotenv import load_dotenv
import os
from os import environ

load_dotenv()
KEY = os.getenv('KEY')


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = KEY
ALLOWED_HOSTS = ['localhost','127.0.0.1','0.0.0.0','helpfinity.app']
DEBUG = os.getenv("DEBUG") == "False"
JWT_SECRET = os.getenv("JWT_SECRET", default=SECRET_KEY)
SITE_ID = 2
AUTH_USER_MODEL = "accounts.User"


if os.getenv("STAGE") == "PRODUCTION":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("POSTGRES_DB"),
            "USER": os.getenv("POSTGRES_USER"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
            "HOST": "annapurna.liara.cloud",
            "PORT": 31496,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


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
    "storages",
    "rest_framework_swagger",
    "drf_yasg",
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




# S3 Settings
LIARA_ENDPOINT="https://storage.c2.liara.space"
LIARA_BUCKET_NAME="helpfinity"
LIARA_ACCESS_KEY="aq5pfn7fo81ddara"
LIARA_SECRET_KEY="2146eea4-e813-4d2a-a4f0-f4b69377a8cd"

# S3 Settings Based on AWS (optional)
AWS_ACCESS_KEY_ID = LIARA_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = LIARA_SECRET_KEY
AWS_STORAGE_BUCKET_NAME = LIARA_BUCKET_NAME
AWS_S3_ENDPOINT_URL = LIARA_ENDPOINT
AWS_S3_REGION_NAME = 'us-east-1'


# Django-storages configuration
STORAGES = {
  "default": {
      "BACKEND": "storages.backends.s3.S3Storage",
  },
  "staticfiles": {
      "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
  },
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Tehran"
USE_I18N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.getenv("STATIC_ROOT", default="/static/")
STATIC_URL = os.getenv("STATIC_URL", default="/static/")
MEDIA_ROOT = "https://helpfinity.storage.c2.liara.space/media/"
MEDIA_URL = "https://helpfinity.storage.c2.liara.space/media/"
#STATICFILES_DIRS = ["docs/"]


# OTP CONFIGURATION
OTP_CODE_LENGTH = int(os.getenv("OTP_CODE_LENGTH", default="4"))
OTP_TTL = int(os.getenv("OTP_TTL", default="120"))
# END OTP CONFIGURATION

# JWT SETIINGS
ACCESS_TTL = int(os.getenv("ACCESS_TTL", default="3"))  # days
REFRESH_TTL = int(os.getenv("REFRESH_TTL", default="7"))  # days
# END JWT SETTINGS




'''
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'drf_social_oauth2.backends.DjangoOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
'''

# Google Configuration
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "366111965494-bbgflimp8s9dtndoufsah3v235bt8lhh.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "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"
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'https://api.helpfinity.app/google-redirect/'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]




# REST FRAMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "accounts.backends.JWTAuthentication",
        #"rest_framework.authentication.TokenAuthentication",
        #"rest_framework.authentication.SessionAuthentication",
        #"oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        #"drf_social_oauth2.authentication.SocialAuthentication",
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_THROTTLE_RATES": {"otp": os.getenv("OTP_THROTTLE_RATE", default="10/min"), },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# END REST FRAMEWORK CONFIGURATION


# CORSHEADERS CONFIGURATION
domain_list = ["https://helpfinity.app","https://liara.run","http://localhost","http://127.0.0.1","https://api.helpfinity.app","https://.helpfinity.app"]
CORS_ALLOWED_ORIGINS = domain_list
CSRF_TRUSTED_ORIGINS = domain_list
CORS_ORIGIN_WHITELIST = domain_list
CORS_ORIGIN_ALLOW_ALL = True
#CORS_REPLACE_HTTPS_REFERER = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SECURE=True
#CSRF_COOKIE_SECURE = False
#CSRF_COOKIE_HTTPONLY = False
#SESSION_COOKIE_SAMESITE = False
#SESSION_COOKIE_DOMAIN = "http://195.214.235.46"
# END CORSHEADERS CONFIGURATION

APPEND_SLASH = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

