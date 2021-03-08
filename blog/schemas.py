from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    content: str

class Blog(BlogBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    username: str
    password: str

class UserResponse(BaseModel):
    name: str
    username: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class BlogResponse(BaseModel):
    title: str
    content: str
    author: UserResponse = None
    
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None




