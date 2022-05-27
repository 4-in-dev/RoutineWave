from achievement.models import Achievement, Status, Rank
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
            'writer',
            'hp',
            'int',
            'money',
            'ten',
            'exp',
            'will',
        )


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = (
            'writer',
            'rank',
            'finished_schedules',
        )