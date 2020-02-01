from django.db import models
from posts.models import Post
import datetime

def image_directory_path(instance, filename):
    return f'posts/images/{instance.id}-{datetime.datetime.now().strftime("%y%m%d%H:%M:%S")}.jpg'


class Image(models.Model):
    post = models.ForeignKey(Post, verbose_name='게시글', on_delete=models.CASCADE,
                             related_name='images', blank=True, null=True)
    created_at = models.DateField('작성시간', auto_now_add=True)
    url = models.ImageField(upload_to=image_directory_path)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.post.title
