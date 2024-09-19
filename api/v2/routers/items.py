from fastapi import APIRouter
from typing import Optional

import uuid


router = APIRouter()


ITEMS = [
    {
        "id": uuid.uuid4(),
        "title": "Item 1",
        "weight": 20.0
    },
    {
        "id": uuid.uuid4(),
        "title": "Item 2",
        "weight": 15.5
    }
]


@router.get("/{item_id}")
async def get_items(item_id: Optional[uuid.UUID] = None):
    if item_id is None:
        return ITEMS

    for item in ITEMS:
        if item["id"] == item_id:
            return item
