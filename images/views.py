from django.core.files.storage import default_storage
from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics
from posts.models import Post
from dailypicture.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated


class ImageCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        post_id = self.request.data['post']
        post = Post.objects.get(pk=post_id)
        super().perform_create(serializer)
        serializer.save(post=post)
        return


class ImageDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_destroy(self, instance):
        instance.url.delete(save=False)
        instance.delete()
