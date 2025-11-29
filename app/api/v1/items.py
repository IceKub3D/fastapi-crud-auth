# app/api/v1/items.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class Item(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

@router.get("/", response_model=list[Item])
async def list_items():
    return [
        {"id": 1, "title": "Example item", "description": "A stub item"}
    ]

