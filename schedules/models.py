from django.db import models

from users.models import User

# 스케쥴과 스케쥴 카테고리 등록

DEFAULT_CATEGORY = "카테고리 없음"


class Category(models.Model):
    title = models.CharField(max_length=255, default=DEFAULT_CATEGORY)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Schedule(models.Model):
    created_by = models.ForeignKey('users.User', related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    schedule_date = models.DateTimeField('custom date')
    content = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField('완료 여부', default=False)

    start_time = models.DateTimeField('start_time')
    end_time = models.DateTimeField('end_time')

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(Category, related_name='schedules', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = "schedule"
        verbose_name = "스케쥴 조각"
        verbose_name_plural = "{} {}".format(verbose_name, "목록")