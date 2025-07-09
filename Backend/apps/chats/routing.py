from django.urls import re_path
from apps.chats.consumer import ChatConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<group_id>\w+)/$', ChatConsumer.as_asgi())
]