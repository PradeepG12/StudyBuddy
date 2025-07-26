"""
ASGI config for base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')
django.setup()
# from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.common.middleware import JWTMiddleware
from apps.chats.routing import websocket_urlpatterns


application = ProtocolTypeRouter({
    "websocket": JWTMiddleware(
        URLRouter(websocket_urlpatterns)
    )
})
