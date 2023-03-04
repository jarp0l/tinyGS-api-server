import httpx
from fastapi import APIRouter, Query, status

from app.schemas import UserCreate, UserRead, VerifyResponseSchema
from app.users import auth_backend, fastapi_users
from app.utils.config import CONFIG


TOKEN_VERIFY_URL = CONFIG.api_token_verify_url


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
router.include_router(
    fastapi_users.get_reset_password_router(),
)
router.include_router(
    fastapi_users.get_verify_router(UserRead),
)


@router.get(
    "/verify",
    status_code=status.HTTP_200_OK,
    response_model=VerifyResponseSchema,
    name="verify:verify-token",
)
def get_verify_token(
    token: str = Query(...),
):
    try:
        response = httpx.post(TOKEN_VERIFY_URL, json={"token": token})
        if response.status_code == 200 and response.json()["is_verified"]:
            return {"detail": "ACCOUNT_VERIFIED"}
        elif response.status_code == 400:
            return response.json()
    except Exception as e:
        raise e
