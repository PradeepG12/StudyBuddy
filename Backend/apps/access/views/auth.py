from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import authenticate

from apps.common.views import AppAPIView

class LoginAPIView(AppAPIView):

    def post(self, request):

        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(email=email, password=password)
        if not user:
            self.send_error_response({"error":"User Not Found"})
        
        refresh = RefreshToken.for_user(user)
        response = self.send_response({
            "message":"Login Successful",
            "user": user.id
        })
        response.set_cookie("access_token", str(refresh.access_token), httponly=True)
        response.set_cookie("refresh_token", str(refresh), httponly=True)
        return response

