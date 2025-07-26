from django.db import models
from apps.common.models import BaseModel
from apps.access.models import User
from apps.groups.models import Group


class GroupMessage(BaseModel):
    """"""
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        default_related_name = "related_group_messages"


class PrivateMessage(BaseModel):
    """"""

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chat_receiver")
    content = models.TextField()

    class Meta:
        default_related_name = "related_private_messages"