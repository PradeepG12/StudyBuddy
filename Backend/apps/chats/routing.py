from django.urls import path
from apps.chats.consumers import GroupChatConsumer, PrivateChatConsumer

URL_PREFIX = "ws/chat/api"

websocket_urlpatterns = [
    path(f"{URL_PREFIX}/group/<int:group_id>/", GroupChatConsumer.as_asgi()),
    path(f"{URL_PREFIX}/private/<int:receiver_id>/", PrivateChatConsumer.as_asgi()),
]