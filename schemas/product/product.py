from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime
from schemas.common.common import ResponseModel, validate_name
from schemas.user.user import UserResponseModel
from schemas.category.category import CategoryResponseModel
from schemas.supplier.supplier import SupplierResponseModel
from decimal import Decimal
#Attribute Product
#Attribute for create a new product
class ProductRequestModel(BaseModel):
    User: int
    Name: str
    Description: str
    Category: int
    Supplier: int
    Price_Unit: Decimal
    Stock_Quantity: int
    Stock_Min: int
    State: bool = True
    Creation_Date: datetime
    Update_Date: datetime
    
    #Agergar las validaciones de los atributos
    @field_validator('Name')
    @classmethod
    def validate_name(cls, Name):
        return validate_name(Name)
    
    @field_validator('Description')
    @classmethod
    def validate_description(cls, Description):
        if len(Description) < 10:
            raise ValueError("La descripción debe contener al menos 10 caracteres")
        return Description
    
    @field_validator('Price_Unit')
    @classmethod
    def validate_price_unit(cls, Price_Unit):
        if Price_Unit <= 0:
            raise ValueError("El precio unitario debe ser mayor a 0")
        return Price_Unit
    
    @field_validator('Stock_Quantity')
    @classmethod
    def validate_stock_quantity(cls, Stock_Quantity):
        if Stock_Quantity < 0:
            raise ValueError("La cantidad de stock no puede ser negativa")
        return Stock_Quantity
    
    @field_validator('Stock_Min')
    @classmethod
    def validate_stock_min(cls, Stock_Min):
        if Stock_Min < 0:
            raise ValueError("La cantidad mínima de stock no puede ser negativa")
        return Stock_Min
    
#Attribute for response a new create product
class ProductResponseModel(ResponseModel):
    id: int
    User: UserResponseModel
    Name: str
    Description: str
    Category: CategoryResponseModel
    Supplier: SupplierResponseModel
    Price_Unit: Decimal
    Stock_Quantity: int
    Stock_Min: int
    State: bool = True
    Creation_Date: datetime 
    Update_Date: datetime


