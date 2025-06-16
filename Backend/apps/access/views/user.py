from rest_framework import status

from apps.common.views import AppAPIView
from apps.access.models import User
from apps.access.serializers import SignupSerializer


class SignUpApiView(AppAPIView):

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.get_valid_serializer(data=request.data)
        serializer.save()
        return self.send_response({"message":serializer.data}, status_code=status.HTTP_201_CREATED)