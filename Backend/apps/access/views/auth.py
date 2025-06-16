from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError # type: ignore
from rest_framework import status

from apps.common.views import AppAPIView

class LoginAPIView(AppAPIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if not user:
            return self.send_error_response({"error":"User Not Found"})
        refresh = RefreshToken.for_user(user)
        self.send_response({
            "message":"Login Successful",
            "user": user.id,
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh)
        })


class TokenRefreshAPIView(AppAPIView):

    def post(self, request):

        refresh_token = request.data.get("refresh_token")
        try:
            refresh = RefreshToken(refresh_token)
            self.send_response({
                "access_token": str(refresh.access_token)
            })
        except (TokenError, InvalidToken):
            return self.send_response({"Detail":"Invalid Credentials"}, status_code=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(AppAPIView):

    def post(self, request):

        try:
            refresh_token = request.data.get("refresh_token")
            token = RefreshToken(refresh_token)
            token.blacklist()
            self.send_response({"message":"Logged out successfully"},status_code=status.HTTP_205_RESET_CONTENT)
        except(TokenError, InvalidToken):
            return self.send_error_response({"error":"Invalid Credintials"}, status_code=status.HTTP_404_NOT_FOUND)
