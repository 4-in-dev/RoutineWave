from api import serializers
from schedules.models import Schedule


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'id',
            'writer',
            'is_finished',
            'status',
            "start_date",
            "start_time",
            "end_date",
            "end_time",
        )
