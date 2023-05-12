from rest_framework import generics
from organisation_app.permissions import IsOwnerOrReadOnly
from .models import Calendar
from .serializers import CalendarSerializer


class CalendarList(generics.ListAPIView):
    """
    List all calendars.
    No create view as calendar creation is handled by django signals.
    """

    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a calendar if you're the owner.
    """

    permission_classes = [IsOwnerOrReadOnly]

    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
