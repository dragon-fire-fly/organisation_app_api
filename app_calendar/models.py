from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Calendar(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

def create_calendar(sender, instance, created, **kwargs):
    if created:
        Calendar.objects.create(owner=instance)


post_save.connect(create_calendar, sender=User)
