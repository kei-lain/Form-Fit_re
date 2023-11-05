from django.db import models
from authentication.models import Person

class Workout(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    workout = models.CharField()
    targetArea = models.TextField()
    equipment = models.TextField()
    bodypart = models.TextField()
    instructions = models.TextField()