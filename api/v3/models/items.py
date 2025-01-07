from pydantic import BaseModel


class Item(BaseModel):
    """Item model."""
    id: int
    title: str
    weight: float
    height: float
    width: float
