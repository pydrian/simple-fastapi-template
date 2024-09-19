from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from starlette import status
from typing import Union


router = APIRouter()


ITEMS = [
    {
        "id": 1,
        "title": "Item 1",
        "weight": 20.0
    },
    {
        "id": 2,
        "title": "Item 2",
        "weight": 15.5
    }
]


@router.get("")
async def get_items() -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content=ITEMS)


@router.get("/{item_id}")
async def get_item(item_id: int) -> Union[JSONResponse, HTTPException]:
    for item in ITEMS:
        if item["id"] == item_id:
            return JSONResponse(status_code=status.HTTP_200_OK,
                                content=item)

    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                         detail="Item not found.")
