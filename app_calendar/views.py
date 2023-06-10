from rest_framework import generics, permissions, filters
from organisation_app.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Calendar
from .serializers import CalendarSerializer, UserCalendarSerializer


class CalendarList(generics.ListAPIView):
    """
    List all calendars.
    No create view as calendar creation is handled by django signals.
    """

    queryset = Calendar.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CalendarSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # 'likes__owner__profile',
        "owner__calendar",
    ]


class CalendarDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a calendar if you're the owner.
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Calendar.objects.all()
    serializer_class = UserCalendarSerializer
