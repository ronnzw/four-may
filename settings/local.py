from .base import *
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND=config('EMAIL_BACKEND', default='')
EMAIL_HOST=config('EMAIL_HOST', default='')
EMAIL_PORT=config('EMAIL_PORT', default='')
EMAIL_USE_TLS=config('EMAIL_USE_TLS', default='')
EMAIL_HOST_USER=config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL=config('DEFAULT_FROM_EMAIL', default='')