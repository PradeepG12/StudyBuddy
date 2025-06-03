from apps.common.router import AppSimpleRouter
from apps.groups.views import GroupCUDAPIViewset

router=AppSimpleRouter()

router.register('groups/cud', GroupCUDAPIViewset)

urlpatterns = [

]+router.urls