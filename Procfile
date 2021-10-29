web: gunicorn project.routing
celeryworker: celery -A project worker -l INFO & celery -A project beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler & wait -n