from pydantic import BaseModel


class UserListResponse(BaseModel):
    username: str
    first_name: str

    class Config:
        orm_mode = True


class UserLoginRequest(BaseModel):
    username: str
    password: str


class UserRegisterRequest(BaseModel):
    first_name: str
    username: str
    password: str


class UserUpdateRequest(BaseModel):
    first_name: str | None
    last_name: str | None
    nationality: str | None
    bio: str | None
    email: str | None
