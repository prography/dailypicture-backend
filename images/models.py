from django.db import models
from posts.models import Post
import datetime


class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name='게시글', on_delete=models.CASCADE, related_name='images', blank=True,
                             null=True)
    created_at = models.DateTimeField('작성시간', auto_now_add=True)
    url = models.ImageField('사진', upload_to="image_directory_path")

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.post.title


def image_directory_path(instance):
    return "posts/images/{filename}".format(filename=set_filename(instance))


def set_filename(obj):
    return "{uuid}-{time}-{second}.jpg".format(
        uuid=obj.uuid,
        time=datetime.datetime.now(),
        second=datetime.datetime.microsecond(),
    )
