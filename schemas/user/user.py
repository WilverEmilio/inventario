from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from  schemas.common.common import ResponseModel, validate_email
from schemas.employee.employee import EmployeeResponseModel

#Attribute User
#Attribute for create a new user
class UserRequestModel(BaseModel): 
    Employee: int
    User: str
    Password: str
    Role: str
    Email: str
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime
    
    @field_validator("User")
    @classmethod
    def validate_user(cls, User):
        if len(User) < 4:
            raise ValueError("El usuario debe contener al menos 4 caracteres")
        return User
    
    @field_validator("Password")
    @classmethod
    def validate_password(cls, Password):
        if len(Password) < 8:
            raise ValueError("La contraseña debe contener al menos 8 caracteres")
        return Password
    
    @field_validator("Email")
    @classmethod
    def validate_email(cls, Email):
        return validate_email(Email)
    
#Attribute for response a new create user
class UserResponseModel(ResponseModel):
    id: int
    Employee: EmployeeResponseModel
    User: str
    Email: str
    Role: str
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime