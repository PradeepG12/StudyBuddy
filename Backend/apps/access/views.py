from apps.common.views import CUDAPIModelViewSet
from rest_framework import status

from .models import User
from .serializers import SignupSerializer


class SignUpApiViewset(CUDAPIModelViewSet):

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.send_response(self, "Signup successful", status_code=status.HTTP_201_CREATED)
        return self.send_response(self, data=serializer.errors, status_code=status.HTTP_400_BAD_REQUEST)