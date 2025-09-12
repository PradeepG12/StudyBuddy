from rest_framework.generics import get_object_or_404
from apps.groups.models import Group

class RetriveGroupMixin:
    """"""

    def get_group(self):
        """"""

        return get_object_or_404(Group.objects.all(), id=self.kwargs.get("group_id"))