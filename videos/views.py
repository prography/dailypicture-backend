from images.models import Image
from posts.models import Post
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from videos.timelapse import Timelapse


@api_view(["GET"])
def convertVideo(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    images = Image.objects.filter(post_id=pk)
    if len(images) == 0:
        return Response(status=status.HTTP_404_NOT_FOUND)
    img_urls = [img.url for img in images]

    video = Timelapse(img_urls, post.title, str(pk))
    video_url = video.make()

    return Response({"video_url": video_url}, status.HTTP_200_OK)
