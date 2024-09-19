from fastapi import APIRouter

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


@router.get("")
async def get_items():
    return ITEMS
