from django.db import models
from accounts.models import User
import datetime

def image_directory_path(instance, filename):
    return f'account/thumbnail/{datetime.datetime.now().strftime("%y%m%d%H:%M:%S")}.jpg'

class Post(models.Model):
    owner = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE, related_name='my_post')
    created_at = models.DateField('작성시간',auto_now_add=True)
    title = models.CharField('제목',max_length=300)
    thumbnail = models.ImageField('썸네일', upload_to=image_directory_path)
    status = models.BooleanField('상태', default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title