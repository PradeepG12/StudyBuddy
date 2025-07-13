from django.urls import path
from apps.chats.views import GroupMessageListAPIViewSet, PrivateMessageListAPIViewSet
from apps.common.router import AppSimpleRouter

router = AppSimpleRouter()

router.register(r"chat/group/(?P<group_id>\d+)/list", GroupMessageListAPIViewSet ,basename='group-message')
router.register(r"chat/private/(?P<receiver_id>\d+)/list", PrivateMessageListAPIViewSet ,basename='private-message')


urlpatterns = []+ router.urls