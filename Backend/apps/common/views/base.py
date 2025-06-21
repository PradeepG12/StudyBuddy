from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class APIViewMixin:

    permission_classes = [IsAuthenticated]
    
    def get_request(self):
        return self.request
    
    def get_user(self):
        return self.get_request().user
    
    def get_authenticated_user(self):
        user = self.get_user()
        return user if user and user.is_authenticated else None

    @staticmethod
    def send_response(data=None, status_code=status.HTTP_200_OK, **other_response):
        
        return Response({
            "data": data,
            "status": "success" if status.is_success(status_code) else "error"
        },
        status=status_code,
        **other_response,
        )

    @staticmethod
    def send_error_response(error=None, status_code=status.HTTP_400_BAD_REQUEST, **other_response):
        
        return Response({
            "status": "error",
            "error": error
        },
        status=status_code)


class APIModelViewSet(APIViewMixin):
    
    pass


class CUDAPIModelViewSet(APIModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    
    def list(self, request):
        raise MethodNotAllowed("GET request")


class ReadOnlyModelViewset(APIModelViewSet, ListModelMixin, GenericViewSet):

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed("POST is not allowed")


class AppAPIView(APIViewMixin, APIView):
    
    serializer_class = None

    def get_serializer_class(self):
        return self.serializer_class

    def get_serializer_context(self):
        return {"request": self.get_request()}
    
    def get_valid_serializer(self, data=None):

        serializer = self.get_serializer_class()(data=data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        return serializer


class CreateAppAPIView(AppAPIView, CreateAPIView):

    def get(self, request):
        raise MethodNotAllowed("Get Method not allowed")


class ServerStatus(AppAPIView):
    def get(self, *args, **kwargs):
        return self.send_response()