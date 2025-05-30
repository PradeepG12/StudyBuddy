from django.urls import path
from apps.access.views import SignUpApiView, LoginAPIView, LogoutAPIView, TokenRefreshAPIView

urlpatterns=[
    path("signup/", SignUpApiView.as_view()),
]+[
    path("login/", LoginAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("refresh-token/", TokenRefreshAPIView.as_view())
]