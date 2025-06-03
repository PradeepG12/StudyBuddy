from apps.common.views import CUDAPIModelViewSet
from apps.groups.models import Group
from apps.groups.serializer import GroupCreateSerializer

class GroupCUDAPIViewset(CUDAPIModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupCreateSerializer