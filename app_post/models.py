from django.db import models
from django.contrib.auth.models import User
from app_event.models import Event


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, related_name="posts", on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../sd2as2klixs1ijw9022d", blank=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
