from pydantic import BaseModel, field_validator
from typing import Optional
import re
from datetime import datetime
from schemas.common.common import ResponseModel, validate_name, validate_last_name, validate_email

#Attribute Category
#Attribute from create a new category
class CategoryResquiestModel(BaseModel):
    Name: str
    Description: str
    State: bool = True

    #Agergar las validaciones de los atributos
    @field_validator('Name')
    @classmethod
    def validate_name(cls, Name):
        return validate_name(Name)

#Attribute from response a new create category
class CategoryResponseModel(ResponseModel):
    id: int
    Name: str
    Description: str
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime