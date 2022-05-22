from django.contrib.auth.models import User
from rest_framework import serializers

<<<<<<< HEAD
from .models import Schedule, Status

=======
from .models import Category, Schedule, Status

>>>>>>> 27c1ca57d427776de64d643d0d8a07425ab15f5e

# 스케쥴과 스케쥴 카테고리 등록 시리얼라이저

class ScheduleSerializer(serializers.ModelSerializer):
    writer = User

    class Meta:
        model = Schedule
        fields = [
            "id",
            "writer",
            "start_date",
            "start_time",
            "end_date",
            "end_time",
            "content",
            "is_finished",
            "status",
        ]

#
# class ScheduleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             "start_date",
#             "start_time",
#             "end_date",
#             "end_time",
#             "content",
#             "is_finished",
#         ]
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
#
#
# class ScheduleUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             "start_date",
#             "start_time",
#             "end_date",
#             "end_time",
#             "content",
#             "is_finished",
#         ]
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
#

<<<<<<< HEAD
#
# class ScheduleCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             "start_date",
#             "start_time",
#             "end_date",
#             "end_time",
#             "content",
#             "is_finished",
#         ]
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
#
#
# class ScheduleUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = [
#             "start_date",
#             "start_time",
#             "end_date",
#             "end_time",
#             "content",
#             "is_finished",
#         ]
#         extra_kwargs = {
#             "id": {"read_only": True},
#         }
#

=======
>>>>>>> 27c1ca57d427776de64d643d0d8a07425ab15f5e
# class RegistrationSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=50, min_length=6)
#     username = serializers.CharField(max_length=50, min_length=6)
#     password = serializers.CharField(max_length=150, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
#
#     def validate(self, args):
#         email = args.get('email', None)
#         username = args.get('username', None)
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'email': ('email already exists')})
#         if User.objects.filter(username=username).exists():
#             raise serializers.ValidationError({'username': ('username already exists')})
#
#         return super().validate(args)
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)


<<<<<<< HEAD
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title'
#         )
#         model = Category
=======
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category
>>>>>>> 27c1ca57d427776de64d643d0d8a07425ab15f5e


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD
        fields = ('id', 'title')
        model = Status
=======
        fields = (
            'id',
            'title'
        )
        model = Status
>>>>>>> 27c1ca57d427776de64d643d0d8a07425ab15f5e
