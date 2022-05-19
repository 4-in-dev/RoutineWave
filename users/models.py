from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    username = "기타사용자"
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    nick_name = models.CharField(max_length=8, default="nickname")
    profile_img = models.FileField(upload_to="profile_img", blank=True, null=True)

    def __str__(self):
        return self.email
