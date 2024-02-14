bind = "0.0.0.0:8000"
workers = 4

import os
from whitenoise import WhiteNoise
from JSSNUTRITION.settings import BASE_DIR, STATIC_URL

from JSSNUTRITION.wsgi import application

application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'static'))

# Serve static files directly by WhiteNoise
application.add_files(os.path.join(BASE_DIR, 'static'), prefix=STATIC_URL)

# Enable Gzip compression for served files
application.add_files(os.path.join(BASE_DIR, 'static'), prefix=STATIC_URL, gzip=True)
