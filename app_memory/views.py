from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from .models import Memory
from .serializers import MemorySerializer, MemoryDetailSerializer
from organisation_app.permissions import IsOwnerOrReadOnly


class MemoryList(generics.ListCreateAPIView):
    """
    List all memories.
    perform_create method for memory creation.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MemorySerializer
    queryset = Memory.objects.all()
    # filter_backends = [
    #     DjangoFilterBackend,
    # ]
    # filterset_fields = [
    #     "post",
    # ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoryDetailSerializer
    queryset = Memory.objects.all()
