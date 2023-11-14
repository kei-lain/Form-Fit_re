from ninja import Schema, ModelSchema
from pydantic import validator, BaseModel, EmailStr
from pydantic.schema import Optional
import asyncio 
from .models import Workout, Workout_Plan
from authentication.models import Person
from authentication.models import Person
from django.core.exceptions import ValidationError
from ninja.errors import ValidationError as NinjaValidationError

class WorkoutSchema(ModelSchema):
    class Config:
        model = Workout
        model_fields = '__all__'


class PlanSchema(ModelSchema):
    class Config:
        model = Workout_Plan
        model_fields = '__all__'



class NotFoundSchema(Schema):
    msg: str
    

class ErrorSchema(Schema):
    message: str