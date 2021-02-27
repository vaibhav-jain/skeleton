from .base import *

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")
