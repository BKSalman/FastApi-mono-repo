"""
schemas used in multiple apps

"""
from pydantic import BaseModel


class UserResponse(BaseModel):
    id: str
    username: str
    email: str | None
    first_name: str
    last_name: str | None
    nationality: str | None
    bio: str | None

    class Config:
        orm_mode = True


class UserToken(BaseModel):
    access_token: str
    refresh_token: str
