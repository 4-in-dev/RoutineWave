from django.db import models

from users.models import User

# 스케쥴과 스케쥴 카테고리 등록

DEFAULT_CATEGORY = "카테고리 없음"


# class Category(models.Model):
#     title = models.CharField(max_length=255, default=DEFAULT_CATEGORY)
#
#     class Meta:
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.title


class Status(models.Model):
    title = models.CharField(max_length=10, default=DEFAULT_CATEGORY)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=10, default=DEFAULT_CATEGORY)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.title


class Schedule(models.Model):

    STATUS_CHOICES = (
        ('hp', '체력'),
        ('int', '지력'),
        ('will', '근성'),
        ('exp', '경험'),
        ('money', '재력'),
        ('ten', '행복'),
    )

    writer = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, null=True)
    content = models.TextField(null=True, blank=True)
    is_finished = models.BooleanField('완료 여부', default=False)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, null=True, blank=True)

    # status = models.ForeignKey(Status, related_name='status', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='근성')


    class Meta:
        db_table = "schedule"
        verbose_name = "스케쥴 조각"
        verbose_name_plural = "{} {}".format(verbose_name, "목록")