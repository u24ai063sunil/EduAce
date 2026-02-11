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

BASE_DIR = Path(__file__).resolve().parent.parent


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
    'home',
]


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
RESEND_API_KEY = os.environ.get("RESEND_API_KEY")


# =====================
# EMAIL CONFIG (GMAIL SMTP)
# =====================

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = f"EduAce <{EMAIL_HOST_USER}>"

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
