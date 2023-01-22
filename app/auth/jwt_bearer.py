'''
Handle verification of protected route
'''

from typing import Optional
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from jwt_handler import decode_jwt

class JWTBearer(HTTPBearer):
    HTTP_FORBIDDEN = 403
    HTTP_FORBIDDEN_MSG = "Invalid or Expired Token!"

    def __init__(self, auto_error: bool = True) -> None:
        super().__init__(auto_error=auto_error)

    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        credentials: HTTPAuthorizationCredentials = await super().__init__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=self.HTTP_FORBIDDEN, detail=self.HTTP_FORBIDDEN_MSG
                )
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=self.HTTP_FORBIDDEN, detail=self.HTTP_FORBIDDEN_MSG
            )

    def verify_jwt(self, jwt_token: str):
      is_token_valid: bool = False
      payload = decode_jwt(jwt_token)
      if payload:
        is_token_valid = True
      return is_token_valid