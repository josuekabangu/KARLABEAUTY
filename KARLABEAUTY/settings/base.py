import os
from pathlib import Path
import environ

# Définition de BASE_DIR pour référencer la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Initialisation de django-environ
env = environ.Env(
    DEBUG=(bool, False)
)

# Lecture du fichier .env si présent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Paramètres communs
SECRET_KEY = env('DJANGO_SECRET_KEY', default='SECRET_KEY')  # Clé secrète du projet
DEBUG = env('DJANGO_ENVIRONMENT') == 'development'  # Mode debug, activé si DJANGO_ENVIRONMENT est "development"

ALLOWED_HOSTS = ['*']  # Hôtes autorisés

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    # 'accounts',
    # Ajoutez vos applications ici
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Middleware pour servir les fichiers statiques
]

# Configuration de l'URL et des modèles
ROOT_URLCONF = 'KARLABEAUTY.urls'
WSGI_APPLICATION = 'KARLABEAUTY.wsgi.application'

# Configuration des bases de données
DATABASES = {
    'default': env.db(),  # Base de données configurée via les variables d'environnement
}

# Configuration des fichiers statiques
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Répertoire des fichiers statiques
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]  # Répertoire additionnel des fichiers statiques
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# Configuration des fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Répertoire des fichiers médias

# Configuration des templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Répertoire des templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuration des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuration de la langue et du fuseau horaire
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Définition du modèle d'utilisateur personnalisé
# AUTH_USER_MODEL = 'accounts.CustomUser'