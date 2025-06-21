from apps.common.views import CUDAPIModelViewSet, AppAPIView
from apps.groups.models import Group
from apps.groups.serializer import GroupCreateSerializer

class GroupCUDAPIViewset(CUDAPIModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer