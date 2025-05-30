from django.urls import path
from apps.access.views import SignUpApiView, LoginAPIView 

urlpatterns=[
    path("signup/", SignUpApiView.as_view()),
    path("login/", LoginAPIView.as_view())
]