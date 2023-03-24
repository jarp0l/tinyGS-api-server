import httpx
from string import Template
from pydantic import EmailStr

from app.schemas import EmailSchema
from app.utils.config import CONFIG


MAIL_API_URL = CONFIG.mail_api_url
MAIL_API_KEY = CONFIG.mail_api_key
MAIL_DOMAIN = CONFIG.mail_domain
MAIL_SENDER = CONFIG.mail_sender
API_VERIFCATION_PATH = CONFIG.api_verifcation_path
API_PW_RESET_PATH = CONFIG.api_pw_reset_path
TOKEN_VERIFY_URL = CONFIG.api_token_verify_url


verification_email_subject = "Confirm Your Account"
verification_email_body = Template(
    """
    <b>Welcome to TinyGS!</b
    <br/>
    <br/>
    Please confirm your account by <a href="${base_url}${verify_path}?token=${token}">clicking here</a>.
    <br/>
    <br/>
    <i>If you didn't create an account, you can ignore this.</i>
    """
)

# password_reset_email_subject = "Password Reset"
# password_reset_email_body = Template(
#     'Use <a href="${base_url}/${pw_reset_path}?token=${token}">this link</a> to reset your password.'
# )


async def send_verification_email(token: str, user_email: EmailStr):
    email = EmailSchema(
        sender=MAIL_SENDER,
        recipient=user_email,
        subject=verification_email_subject,
        body=verification_email_body.safe_substitute(
            base_url=TOKEN_VERIFY_URL, verify_path=API_VERIFCATION_PATH, token=token
        ),
    )

    async with httpx.AsyncClient() as client:
        return await client.post(
            MAIL_API_URL,
            auth=("api", MAIL_API_KEY),
            data={
                "from": email.sender,
                "to": email.recipient,
                "subject": email.subject,
                "html": email.body,
            },
        )


# def send_password_reset_email(token: str, user_email: str):
#     pass
