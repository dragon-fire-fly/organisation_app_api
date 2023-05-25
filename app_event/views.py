from django.db.models import Count
from organisation_app.permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer, CalendarEventSerializer
from .models import Event
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        watches_count=Count('watches', distinct=True),
        memories_count=Count("memory", distinct=True)
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # 'owner__followed__owner__profile',
        'watches__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        "owner__username",
        "title",
        "content",
        "event_type",
        "location",
    ]
    ordering_fields = [
        'watches_count',
        'watches__created_at',
        'memories_count',
    ]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """

    queryset = Event.objects.annotate(
        watches_count=Count('watches', distinct=True),
        memories_count=Count('memory', distinct=True)
    ).order_by('-created_at')
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer
    

class CalendarEventDetail(generics.ListAPIView):
    """
    Retrieve an event for the calendar.
    """

    queryset = Event.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CalendarEventSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "title"
    ]
    search_fields = [
        "title",
    ]
