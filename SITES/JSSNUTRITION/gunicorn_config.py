bind = "0.0.0.0:8000"
workers = 4

import os

import whitenoise

from JSSNUTRITION.settings import STATIC_ROOT

from JSSNUTRITION.wsgi import application

application = whitenoise(application, root=STATIC_ROOT)

STATIC_URL = '/static/'