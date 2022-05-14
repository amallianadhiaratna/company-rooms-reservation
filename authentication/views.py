import datetime
from django.urls import reverse
from drf_yasg import openapi
import logging
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from .models import Employee
from .renderers import UserRenderer
from .serializers import (
    EmployeeSerializer,
    RegisterSerializer,
    LoginSerializer,
    LogoutSerializer,
)


logger = logging.getLogger(__name__)


class EmployeeAPIView(generics.ListAPIView):
    logger.warning(f'{str(datetime.datetime.now())} : Request to access /employee')
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (permissions.IsAuthenticated,)


class RegisterView(generics.GenericAPIView):
    logger.warning(f'{str(datetime.datetime.now())} : Request to access /employee/register')
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = Employee.objects.get(email=user_data["email"])
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        logger.warning(f'{str(datetime.datetime.now())} : Request to access /employee/login with {request.data}')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        logger.warning(f'{str(datetime.datetime.now())} : Request to access /employee/logout with {request.data}')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
