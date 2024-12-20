from pydantic import BaseModel, Field, EmailStr 

"""
class User(BaseModel):
    id: int | None = Field(gt=0)
    email: str
    username: str
    password: str"""

class RequestCreateUser(BaseModel):
    id: int | None = Field(example=1, gt=0)
    email: EmailStr
    username: str = Field(min_length=2, max_length=20)
    password: str
    
class ResponseUser(BaseModel):
    id: int = Field(gt=0)
    email: EmailStr
    username: str = Field(min_length=2, max_length=20)