from pydantic import BaseModel


class ResortResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class ResortCreateRequest(BaseModel):
    name: str


class UserRequest(BaseModel):
    username: str
    password: str
