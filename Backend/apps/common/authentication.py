from rest_framework_simplejwt.authentication import JWTAuthentication # type:ignore

class JWTAuthenticationFromCookie(JWTAuthentication):
    """
    Custom JWT Authentication class that looks for the JWT token in cookies instead of
    the Authorization header.
    """

    def authenticate(self, request):
        # Look for token in cookie named "access_token"
        raw_token = request.COOKIES.get("access_token")

        if raw_token is None:
            return None  # No token means no authentication here, let other auth methods try

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
