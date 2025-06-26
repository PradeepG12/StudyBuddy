from django.urls import path
from apps.chats.views import GroupMessageListAPIViewSet
from apps.common.router import AppSimpleRouter

router = AppSimpleRouter()

router.register(r"chat/group_(?P<group_id>\d+)/list", GroupMessageListAPIViewSet)

urlpatterns = []+ router.urls