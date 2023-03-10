from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
import webbrowser
from time import sleep


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print("HELLO Pankaj!!!!!!")

# shedule setup
@app.task(bind=True)
def autoupdtsetup(self):
    url = 'http://pendant.herokuapp.com/schedulereceived' #'http://127.0.0.1:8000/schedulereceived'

    while True:
        print("refreshing...")
        webbrowser.open(url, new=0)
        sleep(10)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# Commands for Celery

########  Schedule the tasks than run these commands  #########

# 1. celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
# 2. celery -A myproject worker -l INFO
# 3. python3 manage.py runserver
