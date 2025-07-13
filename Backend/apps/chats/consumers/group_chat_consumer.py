import json
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async                  #type:ignore

from apps.common.consumer import CommonChatConsumer
from apps.groups.models import Group, GroupMembers
from apps.chats.models import GroupMessage


@sync_to_async
def get_group(group_id):
    try:
        return Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return None

@sync_to_async
def is_group_member(user, group):
    if _ := GroupMembers.objects.filter(group=group,user=user).exists():
        return True
    return False

@database_sync_to_async
def save_message(user, group, message):
    GroupMessage.objects.create(sender=user, group=group, content=message)
    return True


class GroupChatConsumer(CommonChatConsumer):

    async def connect(self):
        await super().connect()
        self.group_id = self.scope["url_route"]["kwargs"]["group_id"]
        self.room_group_name = f"chat_{self.group_id}"

        self.group = await get_group(self.group_id)
        if not self.group or not await is_group_member(self.user, self.group):
            await self.send_error("Invalid Group Details")
            return
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.send_to_group(type="chat.join_room")

    async def receive(self, text_data):
        text = json.loads(text_data)
        message = text["message"]
        await self.send_to_group(type="chat_message", message=message)
        await save_message(self.user, self.group, message)

    async def chat_message(self, event):
        await self.send_message(event)

    async def chat_join_room(self, event):
        event.update({
            "message":f"{event['user_name']} is joined :)"
        })
        await self.send_message(event)
