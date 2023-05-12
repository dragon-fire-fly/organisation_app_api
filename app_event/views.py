from .serializers import EventSerializer, EventTimeSerializer
from .models import Event, EventTime
from rest_framework import generics


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer


class EventTimeList(generics.ListCreateAPIView):
    queryset = EventTime.objects.all()
    serializer_class = EventTimeSerializer


class EventTimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventTime.objects.all()
    serializer_class = EventTimeSerializer
