from achievement.models import Achievement
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
