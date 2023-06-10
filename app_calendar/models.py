from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import datetime
import pytz
import requests
import os

if os.path.exists("env.py"):
    import env

# API request for timezone info
TIME_ZONE_TOKEN = os.environ.get("TIME_ZONE_TOKEN")
try:
    # response = requests.get(f'https://timezoneapi.io/api/ip/?token={TIME_ZONE_TOKEN}')
    data = response.json()
    timezone = data["data"]["timezone"]["id"]
except:
    timezone = "UTC"


class Calendar(models.Model):
    owner = models.OneToOneField(
        User, related_name="calendar", on_delete=models.CASCADE
    )
    timezone = models.CharField(max_length=255, default=timezone)

    def __str__(self):
        return f"{self.owner}'s calendar"


def create_calendar(sender, instance, created, **kwargs):
    if created:
        Calendar.objects.create(owner=instance)


post_save.connect(create_calendar, sender=User)
