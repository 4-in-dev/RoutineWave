from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from users.models import User


class CustomRegisterSerializer(RegisterSerializer):
    # 기본 설정 필드: username, password, email
    # 추가 설정 필드: profile_image, nick_name
    nick_name = serializers.CharField(max_length=15, min_length=2, required=True)
    profile_image = serializers.ImageField(use_url=True, required=False)


    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nick_name'] = self.validated_data.get('nick_name', '')
        data['profile_image'] = self.validated_data.get('profile_image', '')
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ['id', 'email', 'password', 'nick_name', 'profile_image']


# class UserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(max_length=50, min_length=6)
#     # username = serializers.CharField(max_length=50, min_length=6)
#     password = serializers.CharField(max_length=150, min_length=6, write_only=True)
#     nick_name = serializers.CharField(max_length=15, min_length=2)
#
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'password', 'nick_name', 'profile_img')
#
#     def validate(self, args):
#         email = args.get('email', None)
#         # username = args.get('username', None)
#         nick_name = args.get('nick_name', None)
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'email': ('email already exists')})
#         # if User.objects.filter(username=username).exists():
#         #     raise serializers.ValidationError({'username': ('username already exists')})
#         if User.objects.filter(nick_name=nick_name).exists():
#             raise serializers.ValidationError({'nick_name': ('nickname already exists')})
#
#         return super().validate(args)
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)