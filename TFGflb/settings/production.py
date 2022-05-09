
# production.py
from .base import *
DEBUG = False
ALLOWED_HOSTS = ['fundacionbernaola.com', '194.116.147.91']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = 'https://fundacionbernaola.com/static/'