from django.contrib import admin
from .models import Calendar
from app_event.models import Event


class EventInLine(admin.TabularInline):
    model = Event.calendars.through


class CalendarAdmin(admin.ModelAdmin):
    list_display = ["owner", "get_events"]
    inlines = [EventInLine]

    def get_events(self, instance):
        return [event for event in instance.events.all()]


admin.site.register(Calendar, CalendarAdmin)
