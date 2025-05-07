from pydantic import BaseModel, field_validator
from datetime import datetime
from schemas.common.common import ResponseModel
from schemas.user.user import UserResponseModel
from schemas.product.product import ProductResponseModel
from schemas.customer.customer import CustomerResponseModel
from decimal import Decimal

#Attribute Sale
#Attribute for create a new sale
class SaleRequiestModel(BaseModel):
    Product: int
    Customer: int
    User: int
    Quantity: int
    Date: datetime
    Observation: str
    Total_Price: Decimal
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime
    #Agergar las validaciones de los atributos
    @field_validator('Quantity')
    @classmethod
    def validate_quantity(cls, Quantity):
        if Quantity <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        return Quantity
    
    @field_validator('Total_Price')
    @classmethod
    def validate_total_price(cls, Total_Price):
        if Total_Price <= 0:
            raise ValueError("El precio total debe ser mayor a 0")
        return Total_Price
    
#Attribute for response a new create sale
class SaleResponseModel(ResponseModel):
    id: int
    Product: ProductResponseModel
    Customer: CustomerResponseModel
    User: UserResponseModel
    Quantity: int
    Date: datetime
    Observation: str
    Total_Price: Decimal
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime