from fastapi import APIRouter
from datetime import date

import uuid


router = APIRouter()


USERS = [
    {
        "id": uuid.uuid4(),
        "username": "user_1",
        "birthday": date(year=2024, month=9, day=22)
    }
]


@router.get("")
async def get_users():
    return USERS
