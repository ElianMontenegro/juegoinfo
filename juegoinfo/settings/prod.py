from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['juegoinfo.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'d867j5amjm2gou',
        'USER': 'ivswsliekrtsit',
        'PASSWORD': 'b13ad16ec48adabc7d89ad06b7fa7f98a4b60a66bc0553248645c8017ca7f141',
        'HOST': 'ec2-35-172-246-19.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

