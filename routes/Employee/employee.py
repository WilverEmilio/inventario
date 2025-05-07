from fastapi import HTTPException, APIRouter, Depends
from schemas.employee.employee import EmployeeResponseModel, EmployeeRequestModel
from app.database import Employee
from typing import List
from datetime import datetime

router = APIRouter(prefix='/employee', tags=['Employee'])

@router.get('', response_model=List[EmployeeResponseModel])
async def get_employees(page:int = 1, limit:int=5):
    employees = Employee.select().paginate(page, limit)
    if not employees:
        raise HTTPException(status_code=404, detail='No employees found')
    return employees

@router.get('/{name}', response_model= EmployeeResponseModel)
async def get_employee(name: str):
    employee = Employee.select().where(Employee.Name == name).first()
    
    if not employee:
        raise HTTPException(status_code=404, detail='Employee not found')
    
    return EmployeeResponseModel.from_orm(employee)

@router.post('', response_model=EmployeeResponseModel)
async def create_employee(employee: EmployeeRequestModel):
    if Employee.select().where(Employee.Phone == employee.Phone).exists():
        raise HTTPException(status_code=400, detail='Phone already exists')
    
    try:
        normalized_name = employee.Name.strip().title()
        normalized_last_name = employee.Last_Name.strip().title()
        
        new_employee = Employee.create(
            Name=normalized_name,
            Last_Name=normalized_last_name,
            Age=employee.Age,
            Phone=employee.Phone,
            State=employee.State
        )
        
        return EmployeeResponseModel.from_orm(new_employee)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating employee: {str(e)}') 
    
@router.put('/{id}', response_model = EmployeeResponseModel)
async def update_employee(id: int, employee_data: EmployeeRequestModel):
    try: 
        employee = Employee.select().where(Employee.id == id).first()
        
        if employee.State == False: 
            raise HTTPException(status_code=400, detail='Employee is inactive')
        if not employee:
            raise HTTPException(status_code=404, detail='Employee not found')
        
        employee.Name = employee_data.Name
        employee.Last_Name = employee_data.Last_Name
        employee.Age = employee_data.Age
        employee.Phone = employee_data.Phone
        employee.State = employee_data.State
        employee.Update_Date = datetime.now()
        employee.save()
        
        return EmployeeResponseModel.from_orm(employee)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating employee: {str(e)}')