from django.db import models

# Create your models here.
from users.models import User


class Achievement(models.Model):
    writer = models.ForeignKey(User, related_name='achievement_writer', on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True),
    created = models.DateTimeField(auto_now_add=True),
    date = models.DateField()

    # 하루 일일 달성도
    total_percent = models.FloatField(default=0)
    # 하루 전체 일정 수
    total_schedules_day = models.IntegerField(default=0)
    # 하루 달성 일정 수
    finished_schedules_day = models.IntegerField(default=0)