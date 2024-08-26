from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


# Create your models here.
class SiteChecker(models.Model):
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Name of user who added monitoring service.",
    )
    slack_url = models.URLField(
        max_length=2000, help_text="Add slack url for get notification"
    )
    web_url = models.URLField(
        max_length=2000, help_text="Add Website url for monitoring"
    )
    url_text = models.CharField(
        max_length=255, default="Site Link", help_text="Text to link web url"
    )
    text = models.CharField(max_length=200, help_text="Text for match in web site")
    frequency = models.DurationField(
        help_text="Set the time interval for the task", default=timedelta(minutes=1)
    )
