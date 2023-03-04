from pydantic import BaseModel, EmailStr
from beanie import PydanticObjectId
from fastapi_users import schemas


class UserRead(schemas.BaseUser[PydanticObjectId]):
    pass


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    pass


class EmailSchema(BaseModel):
    sender: EmailStr
    recipient: EmailStr
    subject: str
    body: str


class VerifyResponseSchema(BaseModel):
    detail: str
