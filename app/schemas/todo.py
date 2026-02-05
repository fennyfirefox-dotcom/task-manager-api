from pydantic import BaseModel
from typing import Optional

class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    is_done: bool = False


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_done: Optional[bool] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_done: bool

    class Config:
        from_attributes = True


