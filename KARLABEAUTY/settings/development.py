# settings/development.py

from .base import *

# Activer le mode debug pour le développement
DEBUG = True

# Ajouter les hôtes autorisés pour le développement
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Configuration des bases de données pour le développement (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# Autres configurations spécifiques au développement
