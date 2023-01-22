from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    username: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_test": {
                "username": "testy",
                "email": "testy@example.com",
                "password": "thisisMypassword",
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_test": {
                "email": "testy@example.com",
                "password": "thisisMypassword",
            }
        }
