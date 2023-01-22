from fastapi import FastAPI, Body
from app.model import UserSchema, UserLoginSchema
from app.auth.jwt_handler import sign_jwt

app = FastAPI()

users = []


def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False


@app.get("/")
def home():
    return {"message": "Hello world!"}


@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user)
    return sign_jwt(user.email)


@app.post("/user/signin", tags=["user"])
def user_signin(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return sign_jwt(user.email)
    else:
        return {"message": "Invalid login credentials"}


# @app.post("/user/:token")
# def user_token(token: str):
#     """
#     Check token sent to user on signup
#     """

#     pass
