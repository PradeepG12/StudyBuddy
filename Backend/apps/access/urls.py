from django.urls import path
from apps.common.router import AppSimpleRouter
from .views import SignUpApiViewset

router = AppSimpleRouter()

router.register('signup', SignUpApiViewset)


urlpatterns=[] + router.urls