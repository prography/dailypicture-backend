from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    uuid = models.CharField('uuid', max_length=100)