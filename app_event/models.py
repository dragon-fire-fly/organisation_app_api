from django.db import models
from django.contrib.auth.models import User

EVENT_TYPES = [
    ("0", "Educational"),
    ("1", "Cultural"),
    ("2", "Recreational"),
    ("3", "Fundraiser"),
    ("4", "Private"),
    ("5", "Work"),
    ("6", "Exhibition"),
    ("7", "Festival"),
    ("8", "Concert"),
    ("9", "Cinema"),
    ("10", "Party"),
    ("11", "Seminar"),
    ("11", "Personal"),
    ("13", "Other"),
]

PRIVACY_TYPES = [
    ("0", "Public"),
    ("1", "Followers only"),
    ("2", "Private"),
]


class Event(models.Model):
    """
    Event model, related to user through owner foreign key.
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="images/", default="../default_post_rgq6aq", blank=True
    )
    event_type = models.CharField(max_length=100, choices=EVENT_TYPES)
    location = models.URLField()
    privacy = models.CharField(max_length=100, choices=PRIVACY_TYPES)
    past = models.BooleanField(null=True)
    notification = models.BooleanField(default=False)


class EventTime(models.Model):
    """
    Event time model, related to event through event_id foreign key.
    """

    event_id = models.ForeignKey(Event, related_name="time", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    all_day = models.BooleanField()
