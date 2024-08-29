import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


app.conf.beat_max_loop_interval = 5
# app.conf.beat_scheduler = "django_celery_beat.schedulers:DatabaseScheduler"
