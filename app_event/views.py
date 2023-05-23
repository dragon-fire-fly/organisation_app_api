from django.db.models import Count
from organisation_app.permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, CalendarEventSerializer
from .models import Event
from rest_framework import generics, permissions


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """

    queryset = Event.objects.annotate(
        memories_count=Count("memories", distinct=True)
    ).order_by("-created_at")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """

    queryset = Event.objects.all().order_by("-created_at")
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer

class CalendarEventDetail(generics.ListAPIView):
    """
    Retrieve an event for the calendar.
    """

    queryset = Event.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CalendarEventSerializer
