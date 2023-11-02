from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)

class Person(AbstractBaseUser):
    username = None
    email = models.EmailField(('email address'), max_length=254,blank=True, unique = True)
    password = models.CharField(max_length=60, null=True)
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
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
  