from fastapi import APIRouter, HTTPException, status
from datetime import date
from typing import List

from api.v3.models.users import User


router = APIRouter()

USERS = [
    User(id=1, username="user_1", birthday=date(year=2024, month=9, day=22), email="user_1@example.com"),
    User(id=2, username="user_2", birthday=date(year=2022, month=9, day=11), email="user_2@example.com")
]


@router.get("", status_code=status.HTTP_200_OK)
async def get_users() -> List[User]:
    """Get user list."""
    return USERS


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(user_id: int) -> User:
    """
    Get user by id.
    Args:
        user_id: `int`
    """
    for user in USERS:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="User not found.")
