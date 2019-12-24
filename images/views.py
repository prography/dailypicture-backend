from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics
from posts.models import Post


class ImageCreate(generics.CreateAPIView):
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        post_id = self.request.data['post']
        post = Post.objects.get(pk=post_id)
        super().perform_create(serializer)
        serializer.save(post=post)
        return 


class ImageDetail(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

