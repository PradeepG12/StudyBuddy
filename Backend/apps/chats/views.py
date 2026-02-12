from django.db.models import Q

from apps.chats.models import GroupMessage, PrivateMessage
from apps.chats.serializers import GroupMessageListSerializer, PrivateMessageListSerializer
from apps.common.views import ReadOnlyModelViewset
from apps.groups.utils import RetriveGroupMixin


class GroupMessageListAPIViewSet(RetriveGroupMixin, ReadOnlyModelViewset):
    """"""

    serializer_class = GroupMessageListSerializer

    def get_queryset(self):
        """"""

        user = self.get_user()
        group = self.get_group()
        if not group.related_group_members.filter(user=user).exists():
            return self.send_error_response("Only Group Member are Allowed to read.")
        return GroupMessage.objects.filter(group=group)
    

class PrivateMessageListAPIViewSet(ReadOnlyModelViewset):
    """"""

    serializer_class = PrivateMessageListSerializer

    def get_queryset(self):
        user = self.get_user()
        receiver = self.kwargs.get("receiver_id")
        return PrivateMessage.objects.filter(
            Q(sender=user, receiver=receiver) | Q(receiver=user, sender=receiver)
        )