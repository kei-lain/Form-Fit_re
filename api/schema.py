from ninja import Schema, ModelSchema
from .models import Workout
from authentication.models import Person

class WorkoutSchema(ModelSchema):
    class Config:
        model = Workout
        model_fields = '__all__'

class NotFoundSchema(Schema):
    message: str

class ErrorSchema(Schema):
    message: str