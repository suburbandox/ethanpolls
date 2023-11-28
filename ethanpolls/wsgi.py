"""
WSGI config for ethanpolls project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application
sys.path.append("/home/emkline/ethanpolls")
project_folder = os.path.expanduser('~/ethanpolls')  
load_dotenv(os.path.join(project_folder, '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ethanpolls.settings')

application = get_wsgi_application()


