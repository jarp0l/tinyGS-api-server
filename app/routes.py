from beanie import init_beanie
from fastapi import Depends, FastAPI

from app.db import db_name, User
from app.routers import auth, user
from app.users import current_active_user


app = FastAPI()

app.include_router(auth.router)
app.include_router(user.router)


@app.get("/", status_code=200)
async def root():
    return {"message": "Hello, world"}


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    await init_beanie(
        database=db_name,
        document_models=[
            User,
        ],
    )
