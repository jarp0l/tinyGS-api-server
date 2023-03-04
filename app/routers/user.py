from fastapi import APIRouter

from app.schemas import UserRead, UserUpdate
from app.users import fastapi_users


router = APIRouter(
    prefix="/user",
    tags=["users"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)
