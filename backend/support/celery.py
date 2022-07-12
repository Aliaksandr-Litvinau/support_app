from __future__ import absolute_import
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')

app = Celery('support', broker='redis://0.0.0.0:6379/0')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks()
