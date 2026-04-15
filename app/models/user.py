
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime

class UserInDB(BaseModel):
    name: str
    email: str
    hashed_password: str
    followers: list = []
    following: list = []
    created_at: datetime = datetime.utcnow()