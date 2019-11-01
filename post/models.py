from django.db import models
from user.models import User

class Post(models.Model):
    user_id = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE, related_name='my_post')
    created_at = models.DateTimeField('작성시간',auto_now_add=True)
    title = models.CharField('제목',max_length=300)
    thumbnail = models.ImageField('썸네일', upload_to="account/%Y%m%d")
    status = models.BooleanField('상태', default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title