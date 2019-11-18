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

class Imagelist(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
class ImageDetail(generics.RetrieveDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer