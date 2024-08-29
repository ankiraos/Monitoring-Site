from django.contrib import admin
from .models import SiteChecker

# Register your models here.


@admin.register(SiteChecker)
class SiteCheckerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "slack_url",
        "web_url",
        "url_text",
        "text",
        "frequency",
        "status",
    ]
