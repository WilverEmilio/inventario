import re
from pydantic import BaseModel
from playhouse.shortcuts import model_to_dict

class ResponseModel(BaseModel):
    class Config: 
        from_attributes = True 

    @classmethod
    def from_peewee(cls, peewee_instance):
        '''Convierte un objeto Peewee en un modelo Pydantic'''
        return cls(**model_to_dict(peewee_instance, backrefs=True))

def validate_email(email: str) -> str:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError("El correo electrónico no es válido")
    return email

def validate_name(name: str) -> str:
    if len(name) < 2 or not name.replace(" ", "").isalpha():
        raise ValueError("El nombre debe contener al menos 2 caracteres y solo letras")
    return name

def validate_last_name(last_name: str) -> str:
    if len(last_name) < 2 or not last_name.replace(" ", "").isalpha():
        raise ValueError("El apellido debe contener al menos 2 caracteres y solo letras")
    return last_name