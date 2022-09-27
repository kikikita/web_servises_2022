from pydantic import BaseModel


class User(BaseModel):
    name: str
    password: str
    email: str

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                'name':'Nikita',
                'password':'password',
                'email':'nikita@gmail.com',
            }
        }
    