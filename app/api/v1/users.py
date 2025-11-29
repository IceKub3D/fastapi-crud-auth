# app/api/v1/users.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class UserOut(BaseModel):
    id: int
    username: str
    email: Optional[str] = None

