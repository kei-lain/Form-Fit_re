from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from knox import views as knox_views
from django.contrib.auth.models import login

from .models import Person
from .serializers import *


class CreatePersonAPI(CreateAPIView):
    queryset = Person
    serializer_class = CreatePersonSerializer
    permission_classes = [AllowAny]

class UpdatePersonAPI(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = UpdatePersonSerializer

class LoginAPIView(knox_views.LoginView):
    permission_classes = [AllowAny]    
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            login(request, user)
            response = super().post(request, format=None)
        else:
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.data, status=status.HTTP_200_OK)

