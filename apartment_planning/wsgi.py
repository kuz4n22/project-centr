import os, sys


os.environ["DJANGO_SETTINGS_MODULE"] = "apartment_planning.settings"
print('hello_wsgi')

sys.path.append('/home/g/genrikh/project-centr/public_html')
sys.path.append('/home/g/genrikh/venv/project-centr/lib/python3.11/site-packages/')
#sys.path.remove('/usr/lib/python3.11/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "apartment_planning.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()