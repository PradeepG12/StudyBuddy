from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError # type: ignore
from rest_framework import status

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
    

class TokenRefreshAPIView(AppAPIView):

    def post(self, request):

        refresh_token = request.COOKIES.get("refresh_token")
        try:
            refresh = RefreshToken(refresh_token)
            response = self.send_response({
                "Message": "Token Refreshed Successfully"
            })
            response.set_cookie("access_token", str(refresh.access_token))
            return response
        except (TokenError, InvalidToken):
            return self.send_response({"Detail":"Invalid Credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(AppAPIView):

    def post(self, request):
        response = self.send_response({"message":"Logged out successfully"})
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response
