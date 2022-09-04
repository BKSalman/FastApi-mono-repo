from users.app.api.users.models import User
from users.app.api.users.schemas import UserUpdateRequest
from commons.schemas import UserResponse
from users.app.common.dependencies import db_session
from sqlalchemy.orm import Session

from users.app.common.exceptions import InvalidCredentialsException


def update_user_(
    request_user_updates: UserUpdateRequest,
    current_user: UserResponse,
    session: Session = db_session,
) -> UserResponse:
    user: User | None = session.query(User).filter_by(id=current_user.id).first()
    if user is None:
        raise InvalidCredentialsException()

    user.first_name = request_user_updates.first_name
    user.last_name = request_user_updates.last_name
    user.nationality = request_user_updates.nationality
    user.bio = request_user_updates.bio
    user.email = request_user_updates.email

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        nationality=user.nationality,
        bio=user.bio,
    )
