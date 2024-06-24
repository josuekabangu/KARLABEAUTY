# settings/__init__.py

import os

# Détermination de l'environnement (production ou développement) via la variable d'environnement DJANGO_ENVIRONMENT
ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'development')

# Chargement des paramètres appropriés en fonction de l'environnement
if ENVIRONMENT == 'production':
    from .production import *
else:
    from .development import *
