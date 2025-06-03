from django.db import models

from apps.common.models import BaseModel
from apps.common.config import COMMAN_CHAR_MAX_LENGTH, COMMAN_DEFAULT_NULL_BLANK_CONFIG, COMMAN_DEFAULT_NULL_CONFIG
from apps.access.models import User

class Group(BaseModel):

    name = models.CharField(max_length=COMMAN_CHAR_MAX_LENGTH)
    members = models.ManyToManyField(User)
    description = models.TextField(**COMMAN_DEFAULT_NULL_BLANK_CONFIG)
    admin = models.ManyToManyField(User, related_name="related_group_admins")

    class Meta(BaseModel.Meta):
        default_related_name = "related_groups"
