from django.urls import path
from .views import *

urlpatterns = [
    path('create-user/', CreatePersonAPI.as_view()),
    path('update-user/', UpdatePersonAPI.as_view())
  
]
