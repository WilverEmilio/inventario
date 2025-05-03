from peewee import *
from datetime import datetime
import bcrypt


database = MySQLDatabase('inventorydb',
                         user = 'root',
                         password = '123456789',
                         host = 'localhost',
                         port = 3306)

class Employee(Model):
    Name = CharField(max_length=80)
    Last_Name = CharField(max_length=80)
    Age = IntegerField()
    Phone = CharField(max_length=8)
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        table_name = 'employee'

class User(Model):
    Employee = ForeignKeyField(Employee, backref='user')
    User = CharField(max_length=80, unique=True)
    Password = CharField(max_length=255)
    Role = CharField(max_length=80)
    Email = CharField(max_length=100, unique=True)
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    class Meta: 
        database = database
        table_name = 'user'
        
    @classmethod 
    def create_password(cls, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    @classmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

class Category(Model):
    Name = CharField(max_length=80, unique=True)
    Description = TextField()
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        table_name = 'category'

class Supplier(Model):
    Name = CharField(max_length=80, unique=True)
    Contact_Name = CharField(max_length=80)
    Phone = CharField(max_length=8)
    Address = TextField()
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    class Meta:
        database = database
        table_name = 'supplier'
        
class Product(Model):
    User = ForeignKeyField(User, backref='product')
    Name = CharField(max_length=80, unique=True)
    Description = CharField(max_length=255)
    Category = ForeignKeyField(Category, backref='product')
    Supplier = ForeignKeyField(Supplier, backref='product')
    Price_Unit = DecimalField(max_digits=10, decimal_places=2)
    Stock_Quantity = IntegerField()
    Stock_Min = IntegerField()
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    class Meta: 
        database = database
        table_name = 'product'

class Sale(Model):
    Product = ForeignKeyField(Product, backref='sale')
    User = ForeignKeyField(User, backref='sale')
    Quantity = IntegerField()
    Date = DateTimeField(default=datetime.now)
    Observation = CharField(max_length=255, null=True)
    Total_Price = DecimalField(max_digits=10, decimal_places=2)
    State = BooleanField(default=True)
    Creation_Date = DateTimeField(default=datetime.now)
    Update_Date = DateTimeField(default=datetime.now)
    
    @classmethod
    def get_total_price(cls, product_id, quantity):
        product = Product.get(Product.id == product_id)
        total_price = product.Price_Unit * quantity
        return total_price
    
    @classmethod
    def stock_update(cls, product_id, quantity):
        product = Product.get(Product.id == product_id)
        product.Stock_Quantity -= quantity
        product.save()
        return product.Stock_Quantity
    
    @classmethod
    def stock_recovery(cls, product_id, quantity):
        product = Product.get(Product.id == product_id)
        product.Stock_Quantity += quantity
        product.save()
        return product.Stock_Quantity
    
    class Meta: 
        database = database 
        table_name = 'sale'