from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    """User model."""
    id: int
    username: str
    birthday: date
