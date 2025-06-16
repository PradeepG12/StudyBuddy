from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser

class SerializerMixin:

    def get_request(self):
        return self.context.get("request", None)

    def get_user(self):

        request = self.get_request()
        print(request)
        if request and hasattr(request, 'user'):
            return request.user
        return None


class AppModelSerializer(SerializerMixin, serializers.ModelSerializer):
    
    def create(self, validated_data):
        
        created_by = self.Meta.model._meta.get_field("created_by")
        print(created_by)
        user = self.get_user()
        print(user)
        if created_by and not validated_data.get("created_by") and user and not isinstance(user, AnonymousUser):
            validated_data["created_by"] = user
        instance = super().create(validated_data=validated_data)
        return instance