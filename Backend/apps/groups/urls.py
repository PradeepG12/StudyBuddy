from django.urls import path
from apps.common.router import AppSimpleRouter
from apps.groups.views import GroupCUDAPIViewset, GroupListApiViewSet, GroupJoinExitAPIView, GroupDetailApiViewSet

router=AppSimpleRouter()

router.register('groups/cud', GroupCUDAPIViewset)
router.register('groups/list', GroupListApiViewSet, basename="group-list")
router.register('groups/detail', GroupDetailApiViewSet, basename="group-detail")

urlpatterns = [
    path("join/", GroupJoinExitAPIView.as_view())
]+router.urls