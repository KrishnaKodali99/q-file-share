from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    password: str


class SignUpRequest(BaseModel):
    username: str
    email: str
    password: str