'''
Handle JWT token signing and decoding
'''

import time
import jwt
from decouple import config

JWT_SECRET = config("JWT_SECRET")
JWT_ALGORITHM = config("JWT_ALGORITHM")


def token_response(token: str):
    return {"session": token}


def sign_jwt(userID: str):
    payload = {"userID": userID, "expiry": time.time() + 1800}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decoded_token if decoded_token["expiry"] >= time.time() else None
    except:
        return {}
