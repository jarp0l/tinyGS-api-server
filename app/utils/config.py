from decouple import config
from pydantic import BaseModel


class Settings(BaseModel):
    """Server config settings"""

    # This API server
    server_port = config("SERVER_PORT", default=8081, cast=int)
    client_port = config("CLIENT_PORT", default=3000, cast=int)
    api_verifcation_path = "auth/verify"
    api_pw_reset_path = "auth/reset-password"
    api_token_verify_url = f"http://localhost:{client_port}/auth/verify"

    # Mongo Engine settings
    mongo_uri = config("MONGO_URI", default="mongodb://localhost:27017")
    mongo_dbname = config("MONGO_DBNAME", default="mongodb")

    # Security settings
    jwt_secret = config("JWT_SECRET")

    # Mail settings
    mail_api_url = config("MAIL_API_URL")
    mail_api_key = config("MAIL_API_KEY")
    mail_domain = config("MAIL_DOMAIN")
    mail_sender = config("MAIL_SENDER", default=f"TinyGS <noreply@{mail_domain}>")


CONFIG = Settings()
