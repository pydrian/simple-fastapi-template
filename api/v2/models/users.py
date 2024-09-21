from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    id: int
    username: str
    birthday: date
