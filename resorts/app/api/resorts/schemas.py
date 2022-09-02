from pydantic import BaseModel


class ResortResponse(BaseModel):
    id: str
    name: str

    class Config:
        orm_mode = True


class ResortRequest(BaseModel):
    name: str
