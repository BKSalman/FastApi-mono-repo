from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from users.app.api.users.models import User
from users.app.api.users.exceptions import UserExistsException
from users.app.api.users.schemas import UserRegisterRequest, UserResponse
from users.app.common.utils import get_hashed_password


def create_user_(request_user: UserRegisterRequest, session: Session):
    if session.query(User).filter_by(username=request_user.username).first():
        raise UserExistsException

    if session.query(User).filter_by(username=request_user.username).first():
        raise UserExistsException

    try:
        user: User = User(
            first_name=request_user.first_name,
            username=request_user.username,
            password=get_hashed_password(request_user.password),
        )
        session.add(user)
        session.commit()
    except AssertionError as exception_message:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, exception_message.__str__())

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        nationality=user.nationality,
        bio=user.bio,
    )
