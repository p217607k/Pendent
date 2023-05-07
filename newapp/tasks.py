from django.conf import settings

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection
from django.contrib.auth.models import User
 
from celery import shared_task
from celery.utils.log import get_task_logger

from newapp.views import setup_delete
 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func():
    print("I run every 30 seconds using Celery Beat")
    setup_delete()
    
    return "Done"
 