from apps.common.views import CUDAPIModelViewSet, AppAPIView, ReadOnlyModelViewset
from apps.groups.models import Group
from apps.groups.serializer import GroupCreateSerializer, GroupListSerializer
from apps.groups.config import GroupJoinExitConfig


class GroupCUDAPIViewset(CUDAPIModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer


class GroupListApiViewSet(ReadOnlyModelViewset):
    
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer


class GroupJoinExitAPIView(AppAPIView):

    def post(self, request, *args, **kwargs):

        user = self.get_user()
        operation = request.data.get("operation", None)
        group_id = request.data.get("group",None)
        if not operation and not group_id:
            raise self.send_error_response({"error":"Group ID and Operation must required"})
        group = Group.objects.filter(id=group_id)
        if group and operation in GroupJoinExitConfig.join:
            group.member.set(user)
            group.save()
            return self.send_response({"message":"Joined Successfully"})
        return self.send_error_response({"error":"Somethinng Went Wrong"})