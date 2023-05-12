from django.db import models
from django.contrib.auth.models import User
from app_event.models import Event


class Memory(models.Model):
    """
    Memory model, related to User and Event
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="memories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = models.ImageField(
        upload_to="images/", default="../sd2as2klixs1ijw9022d", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
