from django.db import models
from django import forms

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser



class Person(AbstractBaseUser):
    username = None
    email = models.EmailField(('email address'), max_length=254,blank=True, unique = True)
    password = models.CharField(('password'),max_length=60)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    age = models.PositiveSmallIntegerField()
    GENDER_CHOICES = (
        (1, 'female'),
        (2, 'male'),
        (3, 'other'),

    )
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True)
    weight = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    fitnessgoal = models.TextField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNMAE_FIELD = 'email'

    def __str__(self):
        return self.email
    
    

