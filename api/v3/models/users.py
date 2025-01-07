from pydantic import BaseModel, EmailStr
from datetime import date


class User(BaseModel):
    """User model."""
    id: int
    username: str
    birthday: date
    email: EmailStr
