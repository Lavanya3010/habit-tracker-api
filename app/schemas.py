
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class HabitCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = None
    category: str = Field(default="General", max_length=50)
    frequency: str = Field(default="Daily", max_length=30)
    completed: bool = False


class HabitUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = None
    category: str | None = Field(default=None, max_length=50)
    frequency: str | None = Field(default=None, max_length=30)
    completed: bool | None = None


class HabitResponse(BaseModel):
    id: int
    title: str
    description: str | None
    category: str
    frequency: str
    completed: bool
    created_at: datetime
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
