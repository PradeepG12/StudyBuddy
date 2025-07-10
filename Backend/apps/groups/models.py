from django.db import models

from apps.common.models import BaseModel
from apps.common.config import COMMAN_CHAR_MAX_LENGTH, COMMAN_DEFAULT_NULL_BLANK_CONFIG, COMMAN_DEFAULT_NULL_CONFIG
from apps.access.models import User
from apps.groups.config import GroupRoleTypeChoices

class Group(BaseModel):

    name = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH)
    description = models.TextField(**COMMAN_DEFAULT_NULL_BLANK_CONFIG)

    class Meta(BaseModel.Meta):
        default_related_name = "related_groups"

    @property
    def group_members(self):
        return User.objects.filter(id__in=self.related_group_members.values_list("user", flat=True))
    
    @property
    def group_admin(self):
        return User.objects.filter(id__in=self.related_group_members.filter(role=GroupRoleTypeChoices.admin).values_list("user", flat=True))
    

class GroupMembers(BaseModel):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(choices=GroupRoleTypeChoices, default=GroupRoleTypeChoices.member)
    
    class Meta(BaseModel.Meta):
        default_related_name = "related_group_members"