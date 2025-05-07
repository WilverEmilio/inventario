from fastapi import HTTPException, APIRouter, Depends
from schemas.supplier.supplier import SupplierResponseModel,SupplierRequestModel
from app.database import Supplier
from typing import List
from datetime import datetime

router = APIRouter(prefix='/supplier', tags=['Supplier'])

@router.get('', response_model = List[SupplierResponseModel])
async def get_suppliers(page: int = 1, limit:int =5):
    suppliers = Supplier.select().paginate(page, limit)
    
    if not suppliers:
        raise HTTPException(status_code=404, detail='No suppliers found')
    
    return suppliers

@router.get('/{name}', response_model = SupplierResponseModel)
async def get_supplier(name: str):
    supplier = Supplier.select().where(Supplier.Name == name).first()
    
    if not supplier:
        raise HTTPException(status_code=404, detail='Supplier not found')
    
    return SupplierResponseModel.from_orm(supplier)

@router.post('', response_model=SupplierResponseModel)
async def create_supplier(supplier: SupplierRequestModel):
    normalized_name = supplier.Name.strip().title()
    
    if not normalized_name:
        raise HTTPException(status_code=400, detail='Supplier name cannot be empty')

    if Supplier.select().where(Supplier.Name == normalized_name).exists():
        raise HTTPException(status_code=400, detail='Supplier already exists')
    
    try:
        normalized_contact_name = supplier.Contact_Name.strip().title()
        
        new_supplier = Supplier.create(
            Name=normalized_name,
            Contact_Name=normalized_contact_name,
            Phone=supplier.Phone,
            Address=supplier.Address,
            State=supplier.State
        )
        
        return SupplierResponseModel.from_orm(new_supplier)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating supplier: {str(e)}')
    

@router.put('/{id}', response_model = SupplierResponseModel)
async def update_supplier(id: int, supplier_data: SupplierRequestModel):
    try:
        supplier = Supplier.select().where(Supplier.id == id).first()
        
        if supplier.State == False:
            raise HTTPException(status_code=400, detail='Supplier is inactive')
        if not supplier:
            raise HTTPException(status_code=404, detail='Supplier not found')
        
        supplier.Name = supplier_data.Name
        supplier.Contact_Name = supplier_data.Contact_Name
        supplier.Phone = supplier_data.Phone
        supplier.Address = supplier_data.Address
        supplier.State = supplier_data.State
        
        supplier.save()
        
        return SupplierResponseModel.from_orm(supplier)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating supplier: {str(e)}')