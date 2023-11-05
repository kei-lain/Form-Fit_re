from django.urls import path
from .views import *
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('create-user/', CreatePersonAPI.as_view()),
    path('update-user/', UpdatePersonAPI.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view())
  
]
