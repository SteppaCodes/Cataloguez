from decouple import config
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'cataloguez.settings.{config("SETTINGS")}')

application = get_wsgi_application()
