from pydantic import BaseModel, EmailStr
from typing import Optional

# ---------- Shared Properties ----------
class UserBase(BaseModel):
    email: EmailStr

# ---------- Properties for Creating User ----------
class UserCreate(UserBase):
    password: str

# ---------- Properties for Updating User ----------
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# ---------- Returned to Client ----------
class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True

