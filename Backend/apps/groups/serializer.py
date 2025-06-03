from rest_framework import serializers

from apps.access.models import User
from apps.common.serializers import AppModelSerializer
from apps.groups.models import Group

class GroupCreateSerializer(AppModelSerializer):
    
    members = serializers.PrimaryKeyRelatedField(queryset= User.objects.all(), many=True)
    admin = serializers.PrimaryKeyRelatedField(queryset= User.objects.all(), many=True, required=False)

    class Meta:
        model = Group
        fields = [
            "name",
            "members",
            "description",
            "admin",
        ]
    
    def create(self, validated_data):
        
        user = self.get_user()
        members = validated_data.pop("members",[])
        validated_data.pop("admin",[])
        group = Group.objects.create(**validated_data)
        group.members.set(members)
        group.admin.set([user])
        group.save()
        return group