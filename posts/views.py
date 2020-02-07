from rest_framework import viewsets
from .serializers import *
from dailypicture.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import *

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PostDetailSerializer
        return PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_destroy(self, instance):
        for image in instance.images.all():
            image.url.delete(save=False)
        instance.delete()