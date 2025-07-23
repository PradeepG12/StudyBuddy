import json
from channels.generic.websocket import AsyncWebsocketConsumer #type:ignore
from asgiref.sync import sync_to_async
from apps.access.models import User

class ConsumerMixin:
    """"""
    @sync_to_async
    def get_user_by_id(seld, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None


class CommonChatConsumer(AsyncWebsocketConsumer, ConsumerMixin):
    """"""

    async def connect(self):
        self.user = self.scope.get("user")
        if self.user.is_anonymous:
            await self.send_error("Invalid Authentication.")
        await self.accept()

    async def disconnect(self, *args, **kwargs):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def send_error(self, message):
        await self._send_json({
            "type": "error",
            "message": message,
        })
        await self.close()
        return
    
    async def send_message(self, event: dict):
        await self._send_json({
            "type": event["type"],
            "message": event["message"],
            **event
        })

    async def send_to_group(self, type, message=None,**extra):
        if not hasattr(self, "room_group_name"):
            await self.send_error("Invalid data!")
            return
        event = await self.build_event(type, message, **extra)
        await self.channel_layer.group_send(self.room_group_name, event)

    async def _send_json(self, data):
        await self.send(text_data=json.dumps(data))

    async def build_event(self, type, message, **extra):
        
        from django.utils import timezone

        return {
            "type": type,
            "message": message,
            "user_id": self.user.id,
            "user_name": self.user.first_name,
            "time_zone": timezone.now().isoformat(),
            **extra
        }