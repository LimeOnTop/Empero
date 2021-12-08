# -*- coding: utf-8 -*-
import os, sys

sys.path.insert(0, '/var/www/u1523507/data/www/emprero.com/Emprero')
sys.path.insert(1, '/var/www/u1523507/data/Cloud/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Emprero.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
