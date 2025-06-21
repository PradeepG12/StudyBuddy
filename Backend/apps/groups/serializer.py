from rest_framework import serializers

from apps.groups.config import GroupRoleTypeChoices
from apps.access.models import User
from apps.common.serializers import AppModelSerializer
from apps.groups.models import Group, GroupMembers

class GroupCreateSerializer(AppModelSerializer):
    """"""

    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True,required=False)

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
            "description",
            "members",
        ]

    def create(self, validated_data):
        """"""

        user = self.get_authenticated_user()
        members = validated_data.pop("members", [])
        print(members)
        instance = super().create(validated_data)
        GroupMembers.objects.create(group=instance, user=user, role=GroupRoleTypeChoices.admin)
        group_members = [
            GroupMembers(group=instance, user=member, role=GroupRoleTypeChoices.member)
            for member in members if member != user
            ]
        GroupMembers.objects.bulk_create(group_members)
        return instance
    

class GroupJoinExitSerializer(AppModelSerializer):
    pass