from fastapi import HTTPException, APIRouter
from schemas.product.product import ProductRequestModel, ProductResponseModel
from app.database import Product
from typing import List
from datetime import datetime

router = APIRouter(prefix='/product', tags=['Product'])

@router.get('', response_model = List[ProductResponseModel])
async def get_product(page: int = 1, limit:int =5):
    products = Product.select().paginate(page, limit)
    if not products: 
        raise HTTPException(status_code=404, detail='No products found')
    return products

@router.get('/{product}', response_model = ProductResponseModel)
async def get_product(name: str): 
    product = Product.select().where(Product.Name == name).first()
    
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    
    return ProductResponseModel.from_orm(product)

@router.post('', response_model = ProductResponseModel)
async def create_product(product: ProductRequestModel):
    if Product.select().where(Product.Name == product.Name).exists():
        raise HTTPException(status_code=400, detail='Product already exists')
    
