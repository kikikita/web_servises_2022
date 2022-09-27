from typing import List

from pydantic import BaseModel


class Order(BaseModel):
    username: str
    adress: str
    products: List[str]
    
    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                'username':'Nikita',
                'adress':'Ulitsa Pushkina',
                'products': ['Pizza Margarita'],
            }
        }