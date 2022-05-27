from django.db import models

from users.models import User

# 일일 그래프 달성도
class Achievement(models.Model):

    def __str__(self):
        return str(self.total_percent)

    writer = models.ForeignKey(User, related_name='achievement_writer', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    total_percent = models.FloatField(default=0) # 하루 일일 달성도
    total_schedules_day = models.IntegerField(default=0) # 하루 전체 일정 수
    finished_schedules_day = models.IntegerField(default=0) # 하루 달성 일정 수



# 스텟별 달성도 그래프
class Status(models.Model):

    def __str__(self):
        return str(self.writer)

    writer = models.ForeignKey(User, related_name='status_writer', on_delete=models.CASCADE, null=True)

    hp = models.FloatField(default=0) # 체력(health_point)
    int = models.FloatField(default=0) # 지력(intelligence)
    money = models.FloatField(default=0) # 재력(money)
    ten = models.FloatField(default=0) # 기분, 행복(tension)
    exp = models.FloatField(default=0) # 경험(experience)
    will = models.FloatField(default=0) # 근성(will)



# 사용자별 랭크
class Rank(models.Model):

    def __str__(self):
        return self.rank

    writer = models.ForeignKey(User, related_name='rank_writer', on_delete=models.CASCADE, null=True)
    rank = models.CharField(default='D', max_length=3)
    total_schedules = models.IntegerField(default=0)