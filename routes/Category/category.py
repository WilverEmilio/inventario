from fastapi import HTTPException, APIRouter, Depends
from schemas.category.category import CategoryResponseModel, CategoryResquiestModel
from app.database import Category
from typing import List
from datetime import datetime

router = APIRouter(prefix='/category', tags=['Category'])

@router.get('', response_model = List[CategoryResponseModel])
async def get_categories(page: int = 1, limit: int = 5):
    categories = Category.select().paginate(page, limit)
    if not categories:
        raise HTTPException(status_code=404, detail='No categories found')
    return categories


@router.get('/{name}', response_model = CategoryResponseModel)
async def get_category(name:str):
    categories = Category.select().where(Category.Name == name).first()
    
    if not categories: 
        raise HTTPException(status_code=404, detail='Category not found')
    
    return CategoryResponseModel.from_orm(categories)

@router.post('', response_model = CategoryResponseModel)
async def create_category(category: CategoryResquiestModel):
    if Category.select().where(Category.Name == category.Name).exists():
        raise HTTPException(status_code=400, detail='Category already exists')
    
    try:
        normalized_name = category.Name.strip().title()
        normalized_description = category.Description.strip().title()
        
        new_category = Category.create(
            Name = normalized_name,
            Description = normalized_description,
            State = category.State
        )
        
        return CategoryResponseModel.from_orm(new_category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating category: {str(e)}')
    
@router.put('/{id}', response_model = CategoryResponseModel)
async def update_category(id: int, category_data: CategoryResquiestModel):
    try:
        category = Category.select().where(Category.id == id).first()
        
        if category.State == False:
            raise HTTPException(status_code=400, detail='Category is inactive')
        if not category:
            raise HTTPException(status_code=404, detail='Category not found')
        
        category.Name = category_data.Name
        category.Description = category_data.Description    
        category.State = category_data.State
        category.Update_Date = datetime.now()
        category.save()
        
        return CategoryResponseModel.from_orm(category)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating category: {str(e)}')