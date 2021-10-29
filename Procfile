release: python manage.py migrate
web: gunicorn project.routing
celeryworker: celery -A myproject worker -l INFO & celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler & wait -n