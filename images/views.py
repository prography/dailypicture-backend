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

class Imagelist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ImageDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)