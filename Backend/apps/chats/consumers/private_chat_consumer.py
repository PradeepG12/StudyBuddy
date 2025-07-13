import json
from channels.db import database_sync_to_async      # type:ignore

from apps.common.consumer import CommonChatConsumer
from apps.chats.models import PrivateMessage

@database_sync_to_async
def save_message(sender, receiver, message):
    try:
        PrivateMessage.objects.create(sender=sender, receiver=receiver, content=message)
        return True
    except Exception:
        return False

class PrivateChatConsumer(CommonChatConsumer):
    async def connect(self):
        await super().connect()
        self.receiver_id = self.scope["url_route"]["kwargs"]["receiver_id"]
        if not await self.get_user_by_id(self.receiver_id):
            await self.send_error("Invalid Receiver's Details")
        # TODO: Need to implement different private rooms
        self.room_group_name = await get_room_name(self.receiver_id, self.user.id)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.send_to_group("user_in_chat")
    
    async def receive(self, text_data):
        text = json.loads(text_data)
        await self.send_to_group(type="chat_message", message=text)
        receiver = await self.get_user_by_id(self.receiver_id)
        await save_message(self.user, receiver, text["message"])

    async def chat_message(self, event):
        await self.send_message(event)

    async def user_in_chat(self, event):
        event.update({
            "message": f"{event["user_name"]} is in chat :)"
        })
        await self.send_message(event)

async def get_room_name(user1, user2):
    return f"chat_{min(user1, user2)}-{max(user1, user2)}"
