from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoring_engine.settings')

app = Celery('scoring_engine', broker='pyamqp://scoring_engine:scoring_engine@queue//')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
