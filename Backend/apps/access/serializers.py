from rest_framework import serializers

from apps.common.serializers import AppModelSerializer

from .models import User

class SignupSerializer(AppModelSerializer):
    
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','phone_number']

class BaseUserInfoSerializer(AppModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
        ]

class UserListSerializer(AppModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        ]