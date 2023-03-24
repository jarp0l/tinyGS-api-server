from typing import Optional, Union

from beanie import PydanticObjectId
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, InvalidPasswordException
from fastapi_users.authentication import (
    AuthenticationBackend,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.db import BeanieUserDatabase, ObjectIDIDMixin

from app.db import User, get_user_db
from app.schemas import UserCreate
from app.utils.config import CONFIG

from app.utils.email import send_verification_email


SECRET = CONFIG.jwt_secret


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if (len(password) < 8) or (len(password) > 72):
            raise InvalidPasswordException(
                reason="Password should be between 8 and 72 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(reason="Password should not contain email")

    async def on_after_register(self, user: User):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        # async def send_verification_email(token, email_user):
        #     await print("Emulating email send!")
        print(f"Verification requested for user: {user.id}.")
        try:
            res = await send_verification_email(token, user.email)
            if res.status_code == 200:
                print("Successfully sent!")
            else:
                # print(f"Error sending email! Status code: {res.status_code}")
                raise Exception
        except Exception as e:
            print(f"Error:\n{e}")


async def get_user_manager(user_db: BeanieUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = CookieTransport(cookie_name="token", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])

current_active_user = fastapi_users.current_user(active=True)
