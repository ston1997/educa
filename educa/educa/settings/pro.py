from .base import *

DEBUG = False
ADMINS = (
    ('', ''),
)
ALLOWED_HOSTS = ['www.english-soul.com', 'english-soul.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
