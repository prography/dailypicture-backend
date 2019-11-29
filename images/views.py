# about image application import
# about django rest framework import 
# 2 -> 3 
# add HTTP404
# change apiview module import > decorate > viees
# remove and add mixins / generics
from .models import Image
from posts.models import Post
from .serializers import ImageSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

# from rest_framework import Response
class Imagelist(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    def perform_create(self, serializer):
        serializer.save(post_id_id = self.request.data['post_id'])
        return super().perform_create(serializer)
    

class ImageDetail(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer