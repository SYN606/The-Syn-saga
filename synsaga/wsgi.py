import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "synsaga.settings")

application = get_wsgi_application()

app = application

if os.environ.get('ENV') == 'production':
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
