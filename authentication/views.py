from django.shortcuts import render
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from .models import Person
from .serializers import PersonSerializer , CreatePersonSerializer, UpdatePersonSerializer


class CreatePersonAPI(CreateAPIView):
    queryset = Person
    serializer_class = CreatePersonSerializer
    permission_classes = [AllowAny]

class UpdatePersonAPI(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = UpdatePersonSerializer

