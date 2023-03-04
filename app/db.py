import motor.motor_asyncio
from beanie import PydanticObjectId
from fastapi_users.db import BeanieBaseUser, BeanieUserDatabase

from app.utils.config import CONFIG


DB_NAME = CONFIG.mongo_dbname
DB_URI = CONFIG.mongo_uri

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URI, uuidRepresentation="standard")
db_name = client[DB_NAME]


class User(BeanieBaseUser[PydanticObjectId]):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)
