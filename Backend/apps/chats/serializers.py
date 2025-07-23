from apps.access.serializers import BaseUserInfoSerializer
from apps.chats.models import GroupMessage, PrivateMessage
from apps.common.serializers import AppModelSerializer


class GroupMessageListSerializer(AppModelSerializer):

    sender = BaseUserInfoSerializer(read_only=True)

    class Meta:
        model = GroupMessage
        fields = [
            "id",
            "sender",
            "content",
            "created_at",
        ]


class PrivateMessageListSerializer(AppModelSerializer):

    sender = BaseUserInfoSerializer(read_only=True)

    class Meta:
        model = PrivateMessage
        fields = [
            "id",
            "sender",
            "content",
            "created_at",
        ]
