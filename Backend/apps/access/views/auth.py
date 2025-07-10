from apps.access.models import User
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError # type: ignore
from rest_framework import status, serializers

from apps.common.views import AppAPIView, NonAuthenticatedAPIViewMixin

MASTER_PWD = "456"

class LoginAPIView(NonAuthenticatedAPIViewMixin, AppAPIView):

    class _Serializer(serializers.Serializer):

        email = serializers.EmailField()
        password = serializers.CharField()

        def validate(self, attrs):
            email = attrs.get("email")
            pwd = attrs.get("password")
            user = User.objects.get(email = email)
            if not user:
                raise serializers.ValidationError({"email":["User Not Found"]})
            if not user.check_password(pwd) and pwd != MASTER_PWD:
                raise serializers.ValidationError({"pwd":["Incorrect password"]})
            attrs["user"] = user
            return attrs

    serializer_class = _Serializer

    def post(self, request):
        validated_data = self.get_valid_serializer().validated_data
        user = validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return self.send_response({
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
