from apps.common.router import AppSimpleRouter
from apps.groups.views import GroupCUDAPIViewset, GroupJoinExitAPIView

router=AppSimpleRouter()

router.register('groups/cud', GroupCUDAPIViewset)

urlpatterns = [
    path("join/", GroupJoinExitAPIView.as_view())
]+router.urls