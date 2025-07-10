import json
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer   #type:ignore
from channels.db import database_sync_to_async                  #type:ignore

from apps.groups.models import Group
from apps.chats.models import GroupMessage

@sync_to_async
def get_group(group_id):
    try:
        return Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return None

@database_sync_to_async
def save_message(user, group, message):
    GroupMessage.objects.create(sender=user, group=group, content=message)
    return True


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_id = self.scope["url_route"]["kwargs"]["group_id"]
        self.room_group_name = f"chat_{self.group_id}"
        self.user = self.scope.get("user")

        self.group = await get_group(self.group_id)
        if self.user.is_anonymous or not self.group:
            await self.close()
            return
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        await self.send(text_data=json.dumps({
            "type":"connected",
            "message":f"User {self.user.first_name} is joined.!"
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):

        from django.utils import timezone

        text = json.loads(text_data)
        message = text["message"]
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "user_id": self.user.id,
                "time_zone": timezone.now().isoformat()
            }
        )
        await save_message(self.user, self.group, message)

    async def chat_message(self, event):


        await self.send(text_data=json.dumps({
            "message": event["message"],
            "time_zone": event["time_zone"],
            "user_id": event["user_id"]
        }))

