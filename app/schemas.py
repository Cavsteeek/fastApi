from pydantic import BaseModel, EmailStr
from datetime import datetime

# Posts Schema


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime


# User Schema


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class User(BaseModel):
    email: str


class Config:
    orm_mode = True
