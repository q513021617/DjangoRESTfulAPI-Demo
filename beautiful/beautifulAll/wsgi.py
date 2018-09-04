"""
WSGI config for beautiful project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

sys.path.append("/home/jhon/PycharmProjects/DjangoRESTfulAPI-Demo/beautiful")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beautiful.beautiful.settings")

application = get_wsgi_application()

