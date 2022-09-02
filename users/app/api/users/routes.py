from users.app.common.dependencies import db_session
from fastapi import APIRouter
from sqlalchemy.orm import Session

from .schemas import UserResponse
from .services.list_users import list_users_

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get(
    path="",
    response_model=list[UserResponse],
)
def list_users(
    session: Session = db_session,
):
    return list_users_(session=session)
