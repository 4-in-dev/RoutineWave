from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Schedule

# 스케쥴과 스케쥴 카테고리 등록 시리얼라이저

class ScheduleSerializer(serializers.ModelSerializer):
    writer = User

    class Meta:
        model = Schedule
        fields = [
            "writer",
            "schedule_date",
            "content",
            "is_finished",
            "start_time",
            "end_time",
        ]


class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "schedule_date",
            "content",
            "is_finished",
            "start_time",
            "end_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }


class ScheduleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "schedule_date",
            "content",
            "is_finished",
            "start_time",
            "end_time",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category
