from django.db import models
from django.contrib.auth.models import User
from app_calendar.models import Calendar
import pytz

EVENT_TYPES = [
    ("Educational", "Educational"),
    ("Cultural", "Cultural"),
    ("Recreational", "Recreational"),
    ("Fundraiser", "Fundraiser"),
    ("Private", "Private"),
    ("Work", "Work"),
    ("Exhibition", "Exhibition"),
    ("Festival", "Festival"),
    ("Concert", "Concert"),
    ("Cinema", "Cinema"),
    ("Party", "Party"),
    ("Seminar", "Seminar"),
    ("Personal", "Personal"),
    ("Other", "Other"),
]

PRIVACY_TYPES = [
    ("0", "Public"),
    ("1", "Followers only"),
    ("2", "Private"),
]

TIMEZONES = []
for time in pytz.common_timezones:
    TIMEZONES.append((time, time))


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
        upload_to="images/", default="../sd2as2klixs1ijw9022d", blank=True
    )
    link = models.URLField(null=True, blank=True)
    event_type = models.CharField(
        max_length=100, choices=EVENT_TYPES, default="Educational"
    )
    location = models.CharField(max_length=255)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    all_day = models.BooleanField(default=False)
    privacy = models.CharField(max_length=100, choices=PRIVACY_TYPES)
    past = models.BooleanField(default=False, null=True)
    notification = models.BooleanField(default=False)
    calendars = models.ManyToManyField(Calendar, related_name="events")
    timezone = models.CharField(
        max_length=255, choices=TIMEZONES, default="UTC"
    )

    def get_calendars(self):
        calendars = Calendar.objects.filter(pk=self.owner)
