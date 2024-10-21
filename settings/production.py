from .base import *

DEBUG = False

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Email settings
EMAIL_BACKEND=config('EMAIL_BACKEND', default='')
EMAIL_HOST=config('EMAIL_HOST', default='')
EMAIL_PORT=config('EMAIL_PORT', default='')
EMAIL_USE_TLS=config('EMAIL_USE_TLS', default='')
EMAIL_HOST_USER=config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD=config('EMAIL_HOST_PASSWORD', default='')

