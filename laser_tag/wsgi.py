#wsgi.py
import os, sys
# Calculate the path based on the location of the WSGI script.
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append(project)

# Add the path to 3rd party django application and to django itself.
sys.path.append('/var/www/laser_tag')
os.environ['DJANGO_SETTINGS_MODULE'] = 'laser_tag.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
