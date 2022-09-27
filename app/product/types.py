from pydantic import BaseModel

class Pizza(BaseModel):
    name:str
    description:str|None=None
    price:float

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                'name':'Margarita',
                'description':'Very tasty pizza',
                'price': 700.0
            }
        }