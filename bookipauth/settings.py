from pathlib import Path
from decouple import config
from .juzzmin import JAZZMIN_SETTINGS as JAZZMIN_CONF
from os import path as os_path
from datetime import timedelta

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
    'jazzmin',  # Admin interface customization
    'django.contrib.admin',  # Django admin interface
    'django.contrib.auth',  # User authentication
    'django.contrib.contenttypes',  # Django content type system
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Flash messages
    'django.contrib.staticfiles',  # Static files handling
    'corsheaders',  # Cross-origin resource sharing
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',  # Third-party authentication
    'allauth.account',  # Allauth account management
    'allauth.socialaccount',  # Allauth social account management
    'allauth.socialaccount.providers.google',  # Google login
    'allauth.socialaccount.providers.facebook',  # Facebook login
    'allauth.socialaccount.providers.github',  # GitHub login
    'allauth.socialaccount.providers.microsoft',  # Microsoft login
    'allauth.socialaccount.providers.apple',  # Apple login
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "accounts.apps.AccountsConfig",  # Your custom accounts app
    'drf_yasg',  # Swagger/OpenAPI support
]

# ================================
# Middleware
# ================================

MIDDLEWARE = [
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
        'CONN_MAX_AGE': 700,  # Max connection age for persistent connections
    }
}

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

STATIC_URL = 'static/'  # URL for serving static files
STATIC_ROOT = os_path.join(BASE_DIR, "static")  # Path for static files in production

MEDIA_URL = "/media/"  # URL for serving media files
MEDIA_ROOT = os_path.join(BASE_DIR, "media")  # Path for media files

# ================================
# Admin Customization
# ================================

JAZZMIN_SETTINGS = JAZZMIN_CONF  # Jazzmin settings for the Django admin interface

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Default auto field type for models

# ================================
# Site Configuration
# ================================

SITE_ID = 1  # Default site ID

# ================================
# Authentication Backends
# ================================

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',  # Allauth authentication backend
]

# Django Allauth Settings
ACCOUNT_AUTHENTICATED_REDIRECT_URL = '/'  # Redirect after login
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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'  # Mailgun SMTP host
EMAIL_PORT = 587  # Mailgun SMTP port
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool, default=True)  # Use TLS for email
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  # Mailgun user from environment variables
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')  # Mailgun password from environment variables
MAILGUN_API_KEY = config('MAILGUN_API_KEY')  # Mailgun API key
MAILGUN_DOMAIN = EMAIL_HOST_USER  # Mailgun domain

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Default sender email for allauth

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
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT authentication
        'rest_framework.authentication.SessionAuthentication',  # Optional if you want session-based login too
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',  # Only authenticated users can access
    ],
    'DEFAULT_THROTTLE_CLASSES': [],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/hour',  # Rate limit for user requests
        'anon': '60/minute',  # Rate limit for anonymous requests
    },
}

# ================================
# Custom REST Authentication
# ================================

REST_AUTH = {
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

# ================================
# Social Authentication (Google, Facebook, GitHub, etc.)
# ================================

# OAUTH INTEGRATION
SOCIALACCOUNT_PROVIDERS = {
    'google': {
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
        'SCOPE': [
            'email',
            'public_profile',
        ],
        'AUTH_PARAMS': {
            'auth_type': 'rerequest',
        },
    },
    'github': {
        'SCOPE': ['user', 'email'],
    },
    'microsoft': {
        'SCOPE': ['User.Read'],
    },
    'apple': {
        'SCOPE': ['name', 'email'],
        'CLIENT_ID': config('SOCIAL_AUTH_APPLE_CLIENT_ID'),
        'CLIENT_SECRET': config('SOCIAL_AUTH_APPLE_SECRET'),
        'AUTH_PARAMS': {
            'response_mode': 'form_post',
        },
    },
}

SOCIAL_AUTH_GOOGLE_CLIENT_ID = config('SOCIAL_AUTH_GOOGLE_CLIENT_ID')
SOCIAL_AUTH_GOOGLE_SECRET = config('SOCIAL_AUTH_GOOGLE_SECRET')

SOCIAL_AUTH_FACEBOOK_CLIENT_ID = config('SOCIAL_AUTH_FACEBOOK_CLIENT_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = config('SOCIAL_AUTH_FACEBOOK_SECRET')

SOCIAL_AUTH_GITHUB_CLIENT_ID = config('SOCIAL_AUTH_GITHUB_CLIENT_ID')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_MICROSOFT_CLIENT_ID = config('SOCIAL_AUTH_MICROSOFT_CLIENT_ID')
SOCIAL_AUTH_MICROSOFT_SECRET = config('SOCIAL_AUTH_MICROSOFT_SECRET')

SOCIAL_AUTH_APPLE_CLIENT_ID = config('SOCIAL_AUTH_APPLE_CLIENT_ID')
SOCIAL_AUTH_APPLE_SECRET = config('SOCIAL_AUTH_APPLE_SECRET')
# ================================
# Redis Configuration (commented out)
# ================================

# REDIS_HOST = config('REDIS_HOST', default='localhost')  # Redis host
# REDIS_PORT = config('REDIS_PORT', default=6379)  # Redis port
# REDIS_DB = config('REDIS_DB', default=0)  # Redis database
# REDIS_URL_ADDRESS = config('REDIS_URL_ADDRESS', default='redis://127.0.0.1')  # Redis URL
# REDIS_URL_PORT = config('REDIS_URL_PORT', default=6379)  # Redis port
# REDIS_URL_DB = config('REDIS_URL_DB', default=1)  # Redis DB

# ================================
# CORS Configuration (commented out)
# ================================

# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:3000',  # Frontend development server
#     'https://yourdomain.com',  # Your production domain
# ]
# CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (set to False in production)
# CORS_ALLOW_CREDENTIALS = True  # Allow credentials in CORS requests