from fastapi import FastAPI, APIRouter
from app.database import database as connection
from app.database import (Employee, 
                          User, 
                          Category, 
                          Supplier, 
                          Product, 
                          Sale 
                          )
from starlette.responses import RedirectResponse

app = FastAPI(
    title = "Inventory Management API",
    description = "API for managing inventory, including products, categories, suppliers, and sales.",
    version = "1.0.0",
    contact = {
        "name": "Wilver Emilio Xiá",
        "email": "ixcotwilver@gmail.com"
    }
)

api_version = APIRouter(prefix="/api/v1")

app.include_router(api_version, tags=["API v1"])

@app.on_event("startup")
async def startup():
    if connection.is_closed():
        connection.connect()
    
    connection.create_tables([
        Employee, 
        User, 
        Category, 
        Supplier, 
        Product, 
        Sale
    ])

@app.on_event("shutdown")
async def shutdown():
    if not connection.is_closed():
        connection.close()
    
    print("La conexión a la base de datos se ha cerrado correctamente.")
    
@app.get('/')
async def inicio():
    return RedirectResponse(url='/docs/')