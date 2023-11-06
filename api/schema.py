from ninja import Schema, ModelSchema
from pydantic import validator, BaseModel
from .models import Workout
from authentication.models import Person

class WorkoutSchema(Schema):
    person:  str
    workout: str
    targetArea: str
    equipment: str
    bodypart: str

    
    # @validator(person)

class NotFoundSchema(Schema):
    msg: str
    

class ErrorSchema(Schema):
    message: str