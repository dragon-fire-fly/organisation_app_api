from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from organisation_app.permissions import IsOwnerOrReadOnly


class CommentList(generics.ListCreateAPIView):
    """
    List all comments.
    perform_create method for comment creation.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "post",
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
