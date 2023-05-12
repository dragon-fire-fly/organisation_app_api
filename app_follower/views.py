from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .serializers import FollowerSerializer
from .models import Follower
from organisation_app.permissions import IsOwnerOrReadOnly


class FollowerList(ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
