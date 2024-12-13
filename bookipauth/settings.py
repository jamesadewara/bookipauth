from pathlib import Path
from decouple import config
from .juzzmin import JAZZMIN_SETTINGS as JAZZMIN_CONF
from os import path as os_path
from datetime import timedelta
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ================================
# Project Directory and Paths
# ================================

BASE_DIR = Path(__file__).resolve().parent.parent  # Base directory of the project

# ================================
# Security Settings
# ================================

# Secret key for cryptographic operations (keep it secret in production)
SECRET_KEY = config('SECRET_KEY')  # Ensure this is set in your environment variables

# Encryption key for securing sensitive data (ensure this is set securely)
ENCRYPTION_KEY = config('ENCRYPTION_KEY')

# Debug mode should be False in production for security reasons
DEBUG = config('DEBUG', default=False, cast=bool)

# Hosts allowed to access the Django app (add your production domain here)
ALLOWED_HOSTS = ["127.0.0.1"]

# ================================
# Installed Apps
# ================================
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.github',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'corsheaders',
    'anymail',
    'cloudinary',
    'cloudinary_storage',
    'drf_yasg',
    "accounts.apps.AccountsConfig",
]

# ================================
# Middleware
# ================================

MIDDLEWARE = [
    # 'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Allauth middleware for user sessions
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Handle cross-origin requests
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # XSS protection
]

GZIP_MIN_LENGTH = 200  # Minimum response size (in bytes) to compress

# ================================
# Root URL Configuration
# ================================

ROOT_URLCONF = 'bookipauth.urls'

# ================================
# Templates
# ================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add your template directories if needed
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

# ================================
# WSGI Application
# ================================

WSGI_APPLICATION = 'bookipauth.wsgi.application'

# ================================
# Database Configuration
# ================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # PostgreSQL database engine
        'NAME': config('DATABASE_NAME'),  # Database name from environment variable
        'USER': config('DATABASE_USER'),  # Database user from environment variable
        'PASSWORD': config('DATABASE_PASSWORD'),  # Database password from environment variable
        'HOST': config('DATABASE_HOST', default='localhost'),  # Database host (default is localhost)
        'PORT': config('DATABASE_PORT', default='5432'),  # Database port (default is 5432)
        'CONN_MAX_AGE': 600,  # Max connection age for persistent connections
        # 'OPTIONS': {
        #     'sslmode': 'require',  # Enforce SSL for connections
        # },
    }
}

# Atomic Transactions
# ATOMIC_REQUESTS = True

# ================================
# Password Validation
# ================================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ================================
# Localization
# ================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# ================================
# Static and Media Files
# ================================

STATIC_URL = 'static/'  
STATIC_ROOT = os_path.join(BASE_DIR, "static") 
MEDIA_URL = "/media/"  
MEDIA_ROOT = os_path.join(BASE_DIR, "media")  

# Cloudinary credentials (if using Cloudinary)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', cast=str, default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', cast=str, default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', cast=str, default=''),
    'SECURE': config('CLOUDINARY_SECURE', cast=bool, default=False)
}

# Configure the default file storage
DEFAULT_FILE_STORAGE = config(
    'DEFAULT_FILE_STORAGE',
    default='django.core.files.storage.FileSystemStorage'
)

# ================================
# Admin Customization
# ================================

JAZZMIN_SETTINGS = JAZZMIN_CONF  # Jazzmin settings for the Django admin interface

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default auto field type for models

# ================================
# Authentication Backends
# ================================

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend
]

# Django Allauth Settings
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'
# Configure allauth for email-based authentication
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'  # Options: "mandatory", "optional", or "none"
# Django Allauth settings (can be customized as per your needs)
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1

# ================================
# Email Settings
# ================================
ELASTIC_EMAIL_API_KEY = config('ELASTIC_EMAIL_API_KEY', cast=str)
ELASTIC_EMAIL_API_URL = config('ELASTIC_EMAIL_API_URL', cast=str)
EMAIL_BACKEND = config('EMAIL_BACKEND', cast=str, default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', cast=str, default='smtp.elasticemail.com')
EMAIL_PORT = config('EMAIL_PORT', cast=int, default=587)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str, default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
# ================================
# Simple JWT Settings
# ================================

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),  # Authentication header types (e.g., "Bearer")
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
}
# ================================
# REST Framework Settings
# ================================

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication', 
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Only authenticated users can access
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/hour',  # Rate limit for user requests
        'anon': '60/minute',  # Rate limit for anonymous requests
    },
}

# ================================
# Custom REST Authentication
# ================================

REST_AUTH = {
    'LOGIN_SERIALIZER': 'dj_rest_auth.serializers.LoginSerializer',
    'USER_DETAILS_SERIALIZER': 'dj_rest_auth.serializers.UserDetailsSerializer',
    'REGISTER_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
}

# ================================
# User Model
# ================================

AUTH_USER_MODEL = 'accounts.MainUser'  # Custom user model

# ================================
# Production Settings (Secure)
# ================================

if not DEBUG:
    # Security settings for production
    SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', cast=int, default=31536000)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', cast=bool, default=True)
    SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', cast=bool, default=True)
    SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool, default=False)
    SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', cast=bool, default=True)
    CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', cast=bool, default=True)
    SECURE_CONTENT_TYPE_NOSNIFF = config('SECURE_CONTENT_TYPE_NOSNIFF', cast=bool, default=True)
    SECURE_BROWSER_XSS_FILTER = config('SECURE_BROWSER_XSS_FILTER', cast=bool, default=True)
    X_FRAME_OPTIONS = config('X_FRAME_OPTIONS', cast=str, default="DENY") # Prevent clickjacking attacks

# CROSS ORIGIN
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', cast=bool, default=False)

# Allow Specific Origins
# CORS_ALLOWED_ORIGINS = [
#     "https://example.com",
#     "https://anotherdomain.com",
# ]

# Allow Credentials
CORS_ALLOW_CREDENTIALS = config('CORS_ALLOW_CREDENTIALS', cast=bool, default=False)

# Allow Specific HTTP Methods
# CORS_ALLOW_METHODS = [
#     "GET",
#     "POST",
#     "PUT",
#     "DELETE",
# ]

# Allow Specific Header
# CORS_ALLOW_HEADERS = [
#     "content-type",
#     "authorization",
#     "x-custom-header",
# ]

# ================================
# Social Authentication (Google, Facebook, GitHub, etc.)
# ================================
# ================================
# Site Configuration
# ================================

SITE_ID = 2  # Default site ID

# OAUTH INTEGRATION
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': ''
        },
        'FETCH_USERINFO' : True,
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
    'facebook': {
        'APP': {
            'client_id': config('GOOGLE_CLIENT_ID'),
            'secret': config('GOOGLE_CLIENT_SECRET'),
            'key': ''
        },
        'LOCALE_FUNC': lambda request: 'en_US',
        'METHOD': 'oauth2',  # Set to 'js_sdk' to use the Facebook connect SDK
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
    },
    'github': {
        'APP': {
            'client_id': config('GITHUB_CLIENT_ID'),
            'secret': config('GITHUB_CLIENT_SECRET'),
            'key': ''
        },
        'SCOPE': [
            'user',
            'repo',
            'read:org',
        ],
    },
}
# ================================
# Redis Configuration (commented out)
# ================================
REDIS_URL_ADDRESS = config('REDIS_URL_ADDRESS', default='redis://127.0.0.1')  # Redis URL
REDIS_URL_PORT = config('REDIS_URL_PORT', default=6379)  # Redis port
REDIS_URL_DB = config('REDIS_URL_DB', default=1)  # Redis DB

# REDIS AS CACHE BACKGROUND
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"{REDIS_URL_ADDRESS}/{REDIS_URL_PORT}/{REDIS_URL_DB}",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# Django logging with Redis
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'redis': {
            'level': 'DEBUG',
            'class': 'logstash.TCPLogstashHandler',
            'host': 'redis',
            'port': 6379,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['redis'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}