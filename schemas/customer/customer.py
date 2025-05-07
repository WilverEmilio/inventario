from pydantic import BaseModel, field_validator
from datetime import datetime
from schemas.common.common import ResponseModel, validate_name, validate_email

#Attribute Sale
#Attribute for create a new sale
class CustomerRequestModel(BaseModel):
    Name: str
    Phone: str
    Address: str
    Email: str
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime
    
    #Agergar las validaciones de los atributos
    @field_validator('Name')
    @classmethod
    def validate_name(cls, Name):
        return validate_name(Name)
    
    @field_validator('Phone')
    @classmethod
    def validate_phone(cls, Phone):
        if len(Phone) < 8:
            raise ValueError("El número de teléfono debe contener al menos 10 caracteres")
        return Phone
    
    @field_validator('Address')
    @classmethod
    def validate_address(cls, Address):
        if len(Address) < 10:
            raise ValueError("La dirección debe contener al menos 10 caracteres")
        return Address
    
    @field_validator('Email')
    @classmethod
    def validate_email(cls, Email):
        return validate_email(Email)
    
#Attribute for response a new create sale
class CustomerResponseModel(ResponseModel):
    id: int
    Name: str
    Phone: str
    Address: str
    Email: str
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime