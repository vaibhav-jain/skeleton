import os

import environ
from django.core.wsgi import get_wsgi_application

ENV_FILE = "../.env"
# reading .env file
environ.Env.read_env(ENV_FILE)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_wsgi_application()
