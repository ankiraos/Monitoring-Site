import os
from celery import Celery
from time import sleep

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


@app.task
def add(x, y):
    sleep(10)
    return x + y


app.conf.beat_max_loop_interval = 5
