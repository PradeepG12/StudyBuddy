from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework import status

class APIViewMixin:

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


class APIModelViewSet(APIViewMixin, ModelViewSet):
    pass


class CUDAPIModelViewSet(APIModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    def get(self, request):
        raise MethodNotAllowed("GET request is not allowed")


class ReadOnlyModelViewset(APIModelViewSet, ListModelMixin):

    def create(self, request, *args, **kwargs):
        return MethodNotAllowed("POST is not allowed")


class AppAPIView(APIViewMixin, APIView):
    pass

class CreateAppAPIView(AppAPIView, CreateAPIView):

    def get(self, request):
        raise MethodNotAllowed("Get Method not allowed")

class ServerStatus(AppAPIView):
    def get(self, *args, **kwargs):
        return self.send_response()