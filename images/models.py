from django.db import models
from posts.models import Post

class Image(models.Model):
    post_id = models.ForeignKey(Post, verbose_name='게시글', on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    created_at = models.DateTimeField('작성시간',auto_now_add=True)
    url = models.ImageField('사진', upload_to="posts/images/")

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.post_id.title