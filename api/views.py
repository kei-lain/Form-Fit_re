from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WorkoutSerializer
from authentication.models import Person
from .models import Workout
from .formfit import creatWorkouts



