from rest_framework import generics, permissions
from organisation_app.permissions import IsOwnerOrReadOnly
from .models import Watch
from .serializers import WatchSerializer


class WatchList(generics.ListCreateAPIView):
    """
    List watches or create a watch if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = WatchSerializer
    queryset = Watch.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class WatchDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a watch or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = WatchSerializer
    queryset = Watch.objects.all()
