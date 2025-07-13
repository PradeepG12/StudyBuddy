from apps.chats.models import GroupMessage, PrivateMessage
from apps.chats.serializers import GroupMessageListSerializer, PrivateMessageListSerializer
from apps.common.views import ReadOnlyModelViewset
# from apps.groups.models import GroupMembers


class GroupMessageListAPIViewSet(ReadOnlyModelViewset):
    """"""

    serializer_class = GroupMessageListSerializer

    def get_queryset(self):
        """"""

        user = self.get_user()
        group = self.kwargs.get("group_id") or self.request.query_params.get("group_id")
        # if not GroupMembers.objects.filter(group=group, user=user).exists():
        #     raise PermissionError({"error":"Invalid Details"})
        return GroupMessage.objects.filter(group=group, sender=user)
    

class PrivateMessageListAPIViewSet(ReadOnlyModelViewset):
    """"""

    serializer_class = PrivateMessageListSerializer

    def get_queryset(self):
        user = self.get_user()
        receiver = self.kwargs.get("receiver_id")
        return PrivateMessage.objects.filter(sender=user, receiver=receiver)