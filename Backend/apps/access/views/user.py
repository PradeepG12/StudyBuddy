from rest_framework import status

from apps.common.views import AppAPIView
from apps.access.models import User
from apps.access.serializers import SignupSerializer


class SignUpApiView(AppAPIView):

    queryset = User.objects.all()
    
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return self.send_response({"message":"User Created Successfully"}, status_code=status.HTTP_201_CREATED)
        return self.send_error_response(serializer.errors)