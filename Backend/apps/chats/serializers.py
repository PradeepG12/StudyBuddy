from Backend.apps.chats.models import GroupMessage
from Backend.apps.common.serializers import AppModelSerializer


class GroupMessageListSerializer(AppModelSerializer):

    class Meta:
        model = GroupMessage
        fields = [
            "id",
            "sender",
            "content",
            "created_at",
        ]
