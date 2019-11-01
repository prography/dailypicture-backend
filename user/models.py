from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None,):
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,):
        user = self.create_user(
            username,
            password=password,
        )

        user.is_superuser = True
        user.is_staff = True
        user.nickname = '관리자'
        user.save(using=self._db)
        return user

class User(AbstractUser):
    # username = None
    # email = models.EmailField('이메일', unique=True)
    uuid = models.CharField('uuid', max_length=100)

    REQUIRED_FIELDS = []

    objects = UserManager()
