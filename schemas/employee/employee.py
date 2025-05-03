from pydantic import BaseModel, field_validator
from typing import Optional 
import re
from datetime import datetime 
from schemas.common.common import ResponseModel, validate_name, validate_last_name

#Attribute Employee 
#Attribute from create a new employee
class EmployeeRequestModel(BaseModel):
    Name: str
    Last_Name: str
    Age: int
    Phone: str
    State: bool = True
    
    #Agergar las validaciones de los atributos
    @field_validator('Name')
    @classmethod
    def validate_name(cls, Name):
        return validate_name(Name)
    
    @field_validator('Last_Name')
    @classmethod
    def validate_last_name(cls, Last_Name):
        return validate_last_name(Last_Name)
    
#Attribute from response a new create employee
class EmployeeResponseModel(ResponseModel):
    id: int
    Name: str
    Last_Name: str
    Age: int
    Phone: str
    State: bool = True
    Creation_Date: datetime 
    Update_Date: datetime