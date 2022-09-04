from users.app.api.users.models import User
from users.app.api.users.services.update_user import update_user_
from users.app.common.dependencies import db_session, get_verified_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from users.app.common.exceptions import InvalidCredentialsException

from commons.schemas import UserResponse, UserToken

from .schemas import (
    UserListResponse,
    UserRegisterRequest,
    UserLoginRequest,
    UserUpdateRequest,
)
from .services.list_users import list_users_
from .services.create_user import create_user_
from .services.user_login import user_login_

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get(
    path="",
    response_model=list[UserListResponse],
)
def list_users(
    session: Session = db_session,
):
    return list_users_(session=session)


@users_router.post("", response_model=UserResponse)
def create_user(
    request_user: UserRegisterRequest,
    session: Session = db_session,
):
    return create_user_(request_user, session)


@users_router.post(
    "/login",
    response_model=UserToken,
)
def user_login(
    request_user: UserLoginRequest,
    session: Session = db_session,
):
    return user_login_(request_user, session)


@users_router.get("/me")
def read_current_user(
    current_user: UserResponse = Depends(get_verified_current_user),
    session: Session = db_session,
    # response_model=UserResponse,  # there is a weird error when using this
):
    user: User | None = session.query(User).filter_by(id=current_user.id).first()
    if user is None:
        raise InvalidCredentialsException()
    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        nationality=user.nationality,
        bio=user.bio,
    )


@users_router.patch("")
def update_user(
    request_user_updates: UserUpdateRequest,
    current_user: UserResponse = Depends(get_verified_current_user),
    session: Session = db_session,
):
    return update_user_(request_user_updates, current_user, session)
