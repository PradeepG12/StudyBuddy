from django.urls import path
from apps.common.router import AppSimpleRouter
from apps.groups.views import GroupCUDAPIViewset, GroupListApiViewSet, GroupJoinExitAPIView

router=AppSimpleRouter()

router.register('groups/cud', GroupCUDAPIViewset)
router.register('groups/list', GroupListApiViewSet, basename="group-list")

urlpatterns = [
    path("join/", GroupJoinExitAPIView.as_view())
]+router.urls