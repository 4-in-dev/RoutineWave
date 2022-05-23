from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Scheduletemplate

# 스케쥴과 스케쥴 카테고리 등록 시리얼라이저

class SchedulestemplateSerializer(serializers.ModelSerializer):
    writer = User

    class Meta:
        model = Scheduletemplate
        fields = [
            "id",
            "writer",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "content",
            "is_finished",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


# class StatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title'
#         )
#         model = Status
