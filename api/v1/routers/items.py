from fastapi import APIRouter, status, HTTPException
from typing import List

from api.v1.models.items import Item


router = APIRouter()

ITEMS = [
    Item(id=1, title="Item 1", weight=20.0),
    Item(id=2, title="Item 2", weight=15.5)
]


@router.get("", status_code=status.HTTP_200_OK)
async def get_items() -> List[Item]:
    """Get items."""
    return ITEMS


@router.get("/{item_id}", status_code=status.HTTP_200_OK)
async def get_item(item_id: int) -> Item:
    """Get item by id.
    Args:
        item_id: `int`
    """
    for item in ITEMS:
        if item.id == item_id:
            return item

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Item not found.")
