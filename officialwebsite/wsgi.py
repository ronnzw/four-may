"""
WSGI config for officialwebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# getting environment variables
from decouple import config

# importing whitenoise
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.local' if config('DJANGO_DEBUG', default=False, cast=bool) else 'settings.production')

application = get_wsgi_application()

# wrapping up existing wsgi application
application = WhiteNoise(application, root="staticfiles")
