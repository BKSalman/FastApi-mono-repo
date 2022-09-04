from users.app.api.users.exceptions import IncorrectCredintialsException
from users.app.api.users.models import User
from commons.schemas import UserToken
from users.app.api.users.schemas import UserLoginRequest
from users.app.common.utils import create_access_token, create_refresh_token, get_hashed_password
from sqlalchemy.orm import Session


def user_login_(
    request_user: UserLoginRequest,
    session: Session,
):
    user: User | None = (
        session.query(User)
        .filter_by(username=request_user.username, password=get_hashed_password(request_user.password))
        .first()
    )

    if user is None:
        raise IncorrectCredintialsException()
    return UserToken(
        access_token=create_access_token({"id": user.id, "username": user.username, "first_name": user.first_name}),
        refresh_token=create_refresh_token({"id": user.id, "username": user.username, "first_name": user.first_name}),
    )
