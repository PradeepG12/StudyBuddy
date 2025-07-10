from urllib.parse import parse_qs
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async

User = get_user_model()

@database_sync_to_async
def get_user(validated_token):
    try:
        user_id = validated_token['user_id']
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class JWTMiddleware(BaseMiddleware):
    async def __call__(self, scope, *args, **kwargs):
        query_string = scope['query_string'].decode()
        token_param = parse_qs(query_string).get('token')

        if token_param:
            try:
                validated_token = AccessToken(token_param[0])
                scope['user'] = await get_user(validated_token)
            except Exception:
                scope['user'] = AnonymousUser()
        else:
            scope['user'] = AnonymousUser()
        return await super().__call__(scope, *args, **kwargs)