from django.urls import path
from apps.common.router import AppSimpleRouter
from apps.access.views import SignUpApiView, LoginAPIView, LogoutAPIView, TokenRefreshAPIView, UserListAPIViewSet

router = AppSimpleRouter()

router.register("user/list", UserListAPIViewSet)

urlpatterns=[
    path("signup/", SignUpApiView.as_view()),
]+[
    path("login/", LoginAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("refresh-token/", TokenRefreshAPIView.as_view())
] + router.urls