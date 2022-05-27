from achievement.models import Achievement, Status
from api import serializers



class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'id',
            'writer',
            'date',
            'total_percent',
            "total_schedules_day",
            "finished_schedules_day",
        )



class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = (
            'hp',
            'int',
            'money',
            'ten',
            'exp',
            'will',
        )