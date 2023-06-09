from django.db.models import Count
from organisation_app.permissions import IsOwnerOrReadOnly
from .serializers import EventSerializer
from .models import Event
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


class EventList(generics.ListCreateAPIView):
    """
    List events or create an event if logged in
    The perform_create method associates the event with the logged in user.
    """

    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.annotate(
        watches_count=Count("watches", distinct=True),
        memories_count=Count("memory", distinct=True),
    ).order_by("-created_at")
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "owner__followed__owner__profile",
        "watches__owner__profile",
        "owner__profile",
    ]
    search_fields = [
        "owner__username",
        "title",
        "content",
        "event_type",
        "location",
        "start",
        "end",
    ]
    ordering_fields = [
        "watches_count",
        "watches__created_at",
        "memories_count",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an event and edit or delete it if you own it.
    """

    queryset = Event.objects.annotate(
        watches_count=Count("watches", distinct=True),
        memories_count=Count("memory", distinct=True),
    ).order_by("-created_at")
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer


class EventDetailAddEvent(EventDetail):
    """
    Similar to EventDetail but allows edit from authenticated
    user on calendar field only.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CustomEventPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 1000


class CalendarEvents(generics.ListAPIView):
    """
    Retrieves events from the calendar of the logged in user.
    """

    pagination_class = CustomEventPagination
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = EventSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = [
        "title",
        "owner__profile",
    ]
    search_fields = [
        "title",
    ]
    ordering_fields = ["start"]

    def get_queryset(self):
        queryset = Event.objects.filter(calendars=self.kwargs["pk"]).order_by(
            "start"
        )
        return queryset
