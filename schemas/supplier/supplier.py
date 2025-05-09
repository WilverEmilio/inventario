from pydantic import BaseModel, field_validator
from datetime import datetime
from schemas.common.common import ResponseModel, validate_email, validate_name, validate_last_name

#Attribute Supplier
#Attribute from create a new supplier
class SupplierRequestModel(BaseModel):
    Name : str
    Contact_Name : str
    Phone : str
    Address :  str
    State: bool = True
    
    #Agergar las validaciones de los atributos
    @field_validator('Name')
    @classmethod
    def validate_name(cls, Name):
        return validate_name(Name)
    
#Attribute from response a new create supplier
class SupplierResponseModel(ResponseModel):
    id: int
    Name: str
    Contact_Name: str
    Phone: str
    Address: str
    State: bool = True
    Creation_Date: datetime 
    Update_Date: datetime