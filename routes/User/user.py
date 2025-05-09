from fastapi import HTTPException, APIRouter
from schemas.user.user import UserResponseModel, UserRequestModel
from app.database import User
from typing import List
from datetime import datetime 

router = APIRouter(prefix='/user', tags=['User'])

@router.get('', response_model=List[UserResponseModel])
async def get_user(page: int = 1, limit:int =5):
    users = User.select().paginate(page, limit)
    if not users: 
        raise HTTPException(status_code=404, detail='No users found')
    return users

@router.get('/{user}', response_model = UserResponseModel)
async def get_user_by_username(user: str):
    user = User.select().where(User.User == user).first()
    
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    
    return UserResponseModel.from_orm(user)

@router.post('', response_model = UserResponseModel)
async def create_user(user: UserRequestModel):
    if User.select().where(User.Employee == user.Employee).exists():
        raise HTTPException(status_code=400, detail='Employee already exists')
    if User.select().where(User.User == user.User).exists():
        raise HTTPException(status_code=400, detail='User already exists')
    if User.select().where(User.Email == user.Email).exists():
        raise HTTPException(status_code=400, detail='Email already exists')
        
    try:
        normalized_user = user.User.strip().lower()
        normalized_password = user.Password.strip()
        
        if not normalized_user or not normalized_password:
            raise HTTPException(status_code=400, detail='User and password cannot be empty')
        hashed_password = User.create_password(normalized_password)
        
        new_user = User.create(
            Employee=user.Employee,
            User=user.User,
            Password=hashed_password,
            Role=user.Role,
            Email=user.Email,
            State =user.State,
        )
        
        return UserResponseModel.from_orm(new_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating user: {str(e)}')
    
@router.put('/{id}', response_model = UserResponseModel)
async def update_user(id: int, user_data: UserRequestModel):
    try:
        user = User.select().where(User.id == id).first()
        
        if user.State == False:
            raise HTTPException(status_code=400, detail='User is inactive')
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        
        user.Employee = user_data.Employee
        user.User = user_data.User
        user.Password = User.create_password(user_data.Password)
        user.Role = user_data.Role
        user.Email = user_data.Email
        user.State = user_data.State 
        user.Update_Date = user_data.Update_Date
        
        return UserResponseModel.from_orm(user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating user: {str(e)}')
    finally:
        user.Update_Date = datetime.now()
        user.save()