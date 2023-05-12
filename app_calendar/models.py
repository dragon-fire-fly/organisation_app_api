from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from app_event.models import Event


class Calendar(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event)

def create_calendar(sender, instance, created, **kwargs):
    if created:
        Calendar.objects.create(owner=instance)


post_save.connect(create_calendar, sender=User)
