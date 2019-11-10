from images.models import Image
from posts.models import Post
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import os
import shutil
import cv2
import urllib.request


@api_view(['GET'])
def convertVideo(request, pk):
    images = Image.objects.filter(post_id=pk)
    post = Post.objects.get(pk=pk)
    # 영상 변환부분
    if not os.path.isdir(settings.MEDIA_ROOT + "/video"):
        os.mkdir(os.path.join(settings.MEDIA_ROOT, "video"))

    image_path = "./" + str(pk)
    if not(os.path.isdir(image_path)):
        os.mkdir(image_path)

    for image in images:
        image_url = "http://localhost:8000/media/" + str(image.url)
        urllib.request.urlretrieve(image_url,
                                   os.path.join(image_path,
                                                image_url.split('/')[-1]))


    fps = 60
    imgps = 5

    imgs = [cv2.imread(os.path.join(image_path, image))
            for image in os.listdir(image_path)]
    img_height, img_width, img_channel = imgs[0].shape

    video_file = os.path.join(settings.MEDIA_ROOT,
                              "video",
                              post.title + ".mp4")

    writer = cv2.VideoWriter(video_file,
                             cv2.VideoWriter_fourcc(*"mp4v"),
                             fps,
                             (img_width, img_height))

    for frame in imgs:
        for _ in range(fps//imgps):
            writer.write(frame)
    writer.release()

    if os.path.isdir(image_path):
        shutil.rmtree(image_path)

    video_url = "http://localhost:8000/media/video/" + post.title + ".mp4"
    return Response({"video_url": video_url}, status.HTTP_200_OK)