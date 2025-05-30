from django.urls import path
from apps.common.views import ServerStatus

urlpatterns = [
    path("server/status/", ServerStatus.as_view())
]