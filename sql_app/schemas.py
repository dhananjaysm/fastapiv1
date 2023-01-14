from pydantic import BaseModel
from datetime import datetime, timezone



class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


# class MasterBase(BaseModel):
    # 
class Master(BaseModel):
    id: int
    subjectName: str
    subtopicId: int

    class Config:
        orm_mode = True

class LoggerCreate(BaseModel):
    id:int
    loggedAt: datetime
    type: str
class Logger(BaseModel):
    
    row_id: int
    
    class Config:
        orm_mode = True