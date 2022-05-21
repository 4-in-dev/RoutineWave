from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .managers import UserManager


class User(AbstractUser):

    username = None

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    nick_name = models.CharField(max_length=15)
    # profile_image = models.FileField(upload_to="profile_img/%Y/%m", blank=True, null=True, default='img')

    profile_image = ProcessedImageField(
        blank=True,
        upload_to='profile_image/%Y/%m',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70},
        default='img'
    )

    def __str__(self):
        return self.email

# class Status(models.Model):
#     user_email = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
#     # 체력(HP)
#     health_point = models.IntegerField(default=0)
#     # 지력(INT)
#     intelligence = models.IntegerField(default=0)
#     # 재력(Money)
#     wealth = models.IntegerField(default=0)
#     # 기분, 행복(TEN)
#     tension = models.IntegerField(default=0)
#     # 경험(EXP)
#     experience = models.IntegerField(default=0)
#     # 의지, 정신력(SPI)
#     will = models.IntegerField(default=0)
#
#
#     def __str__(self):
#         return self.email

