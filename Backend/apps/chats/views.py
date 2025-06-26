from apps.chats.models import GroupMessage
from apps.chats.serializers import GroupMessageListSerializer
from apps.common.views import ReadOnlyModelViewset
from apps.groups.models import GroupMembers


class GroupMessageListAPIViewSet(ReadOnlyModelViewset):
    """"""

    serializer_class = GroupMessageListSerializer

    def get_queryset(self):
        """"""

        user = self.get_user()
        group = self.request.query_params.get("group_id")
        if not GroupMembers.objects.filter(group=group, user=user).exists():
            return self.send_error_response({"error":"Invalid Details"})
        return GroupMessage.objects.filter(group=group)