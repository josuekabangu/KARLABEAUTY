from .base import *

# Désactiver le mode debug pour la production
DEBUG = False

# Ajouter les hôtes autorisés pour la production
ALLOWED_HOSTS = ['karlab-325812bf69b1.herokuapp.com']


# Configuration des bases de données pour la production (utilisation de dj-database-url)
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Configuration de la sécurité pour la production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Configuration de la gestion des fichiers statiques avec WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
