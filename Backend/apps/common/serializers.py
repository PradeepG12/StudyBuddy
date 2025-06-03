from rest_framework import serializers
from django.contrib.auth.models import AnonymousUser

class SerializerMixin:

    def get_request(self):
        return self.context.get("request")
    
    def get_user(self):
        return self.get_request().user
    
class AppModelSerializer(SerializerMixin, serializers.ModelSerializer):
    
    def create(self, validated_data):        
        user = self.get_user()
        created_by = self.Meta.model.get_model_feild("created_by")
        if created_by and not validated_data["created_by"] and user and not isinstance(user, AnonymousUser):
            validated_data["created_by"] = user
        return super().create(validated_data)
