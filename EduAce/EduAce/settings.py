# from pathlib import Path
# import os
# # from dotenv import load_dotenv

# # load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent


# # =====================
# # SECURITY
# # =====================

# SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")

# DEBUG =False

# ALLOWED_HOSTS = ["*", ".onrender.com"]


# # =====================
# # APPLICATIONS
# # =====================

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'home',
# ]


# # =====================
# # MIDDLEWARE
# # =====================

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',  # REQUIRED for Render
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# ROOT_URLCONF = 'EduAce.urls'


# # =====================
# # TEMPLATES
# # =====================

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],  # using app templates
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]


# WSGI_APPLICATION = 'EduAce.wsgi.application'


# # =====================
# # DATABASE (SQLite OK for demo)
# # =====================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# # =====================
# # PASSWORD VALIDATION
# # =====================

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]


# # =====================
# # INTERNATIONALIZATION
# # =====================

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True


# # =====================
# # STATIC FILES
# # =====================

# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# STATICFILES_DIRS = [
#     BASE_DIR / "home/static",
# ]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# # =====================
# # AUTH
# # =====================

# LOGIN_URL = '/login/'


# # =====================
# # EMAIL (USE ENV VARS)
# # =====================

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# DEFAULT_FROM_EMAIL = f"EduAce <{EMAIL_HOST_USER}>"



# # =====================
# # OPENROUTER API
# # =====================

# OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")


# # =====================
# # DEFAULT PK
# # =====================

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
from pathlib import Path
import os

# Load .env file into environment for local development (no extra deps)
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
if env_path.exists():
    try:
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' not in line:
                    continue
                key, val = line.split('=', 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                # don't overwrite existing environment variables
                if key not in os.environ:
                    os.environ[key] = val
    except Exception:
        # If loading fails, continue — settings will pick from real env
        pass


# =====================
# SECURITY
# =====================

SECRET_KEY = os.environ.get("SECRET_KEY", "unsafe-dev-key")

DEBUG = False

ALLOWED_HOSTS = [
    "eduace.onrender.com",
    ".onrender.com",
]


# Render HTTPS Fix (VERY IMPORTANT FOR LOGIN)
CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True


# =====================
# APPLICATIONS
# =====================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # User apps (must come before allauth to override templates)
    'home',
    
    # OAuth and authentication
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1


# =====================
# MIDDLEWARE
# =====================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Required on Render
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'EduAce.urls'


# =====================
# TEMPLATES
# =====================

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


WSGI_APPLICATION = 'EduAce.wsgi.application'


# =====================
# DATABASE
# =====================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =====================
# PASSWORD VALIDATION
# =====================

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# =====================
# INTERNATIONALIZATION
# =====================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'   # IMPORTANT (fixes OTP/session time)
USE_I18N = True
USE_TZ = True


# =====================
# STATIC FILES
# =====================

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / "home/static",
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# =====================
# AUTH / SESSIONS
# =====================

LOGIN_URL = '/login/'

SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_SAVE_EVERY_REQUEST = True


# =====================
# EMAIL CONFIG (SendGrid SMTP - for password reset only)
# =====================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# SendGrid SMTP configuration
EMAIL_HOST = os.environ.get("EMAIL_HOST", "smtp.sendgrid.net")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 587))
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# SendGrid: EMAIL_HOST_USER should be "apikey" (literal), EMAIL_HOST_PASSWORD is the API key
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "apikey")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

# Ensure FROM email is valid (fall back to a default if needed)
_from_user = EMAIL_HOST_USER if EMAIL_HOST_USER and "@" in EMAIL_HOST_USER else os.environ.get("SENDGRID_FROM_EMAIL", "noreply@eduace.example.com")
DEFAULT_FROM_EMAIL = f"EduAce <{_from_user}>"

# Prevent worker timeout
EMAIL_TIMEOUT = 5


# =====================
# OPENROUTER API
# =====================

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")


# =====================
# DEFAULT PK
# =====================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =====================
# AUTHENTICATION BACKENDS
# =====================

AUTHENTICATION_BACKENDS = [
    # Django backend
    'django.contrib.auth.backends.ModelBackend',
    
    # Allauth authentication backend
    'allauth.account.auth_backends.AuthenticationBackend',
]

# =====================
# ALLAUTH CONFIGURATION
# =====================

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'  # No email verification - users can signup instantly
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
SOCIALACCOUNT_AUTO_SIGNUP = True

# Redirect after login/logout
LOGIN_REDIRECT_URL = '/features/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/login/'
SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'

# OAuth Provider Settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': os.environ.get('GOOGLE_OAUTH_CLIENT_ID', ''),
            'secret': os.environ.get('GOOGLE_OAUTH_SECRET', ''),
        },
    },
}