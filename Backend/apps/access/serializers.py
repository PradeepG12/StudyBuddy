from rest_framework import serializers

from apps.common.serializers import AppModelSerializer

from .models import User

class SignupSerializer(AppModelSerializer):
    
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','phone_number']