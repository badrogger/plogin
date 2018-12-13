import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plogin',
        'USER': 'ipman',
        'PASSWORD': 'jscrt23',
        'HOST': 'localhost',
        'PORT': '',
    }


}


DEBUG = True
