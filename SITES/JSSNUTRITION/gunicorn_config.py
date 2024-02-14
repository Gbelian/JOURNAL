bind = "0.0.0.0:8000"
workers = 4

import os
from whitenoise import WhiteNoise

from JSSNUTRITION.settings import BASE_DIR, STATIC_URL
from JSSNUTRITION.wsgi import application

# Utilisation de WhiteNoise pour servir les fichiers statiques de manière efficace
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))

# Configuration pour servir les fichiers statiques avec un préfixe défini par STATIC_URL
application.add_files(os.path.join(BASE_DIR, 'static'), prefix=STATIC_URL)

# Activation de la compression Gzip pour les fichiers statiques
application.add_files(os.path.join(BASE_DIR, 'static'), prefix=STATIC_URL, gzip=True)
