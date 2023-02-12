import motor.motor_asyncio
from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from config_manager import get_config

DB_HOST = get_config("MONGODB_HOST")
DB_PORT = get_config("MONGODB_PORT")
DB_USER = get_config("MONGODB_USER")
DB_PASSWORD = get_config("MONGODB_PASSWORD")
DB_NAME = get_config("MONGODB_NAME")

CURRENT_ENV = get_config("ENV")

DATABASE_URL = f"mongodb://{DB_HOST}:{DB_PORT}" if CURRENT_ENV == "dev" else f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}"


client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client[DB_NAME]


class User(BeanieBaseUser[PydanticObjectId]):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
