from sqlalchemy.orm import Session
from users.app.api.users.models import User
from users.app.api.users.schemas import UserListResponse


def list_users_(session: Session) -> list:
    users: list[UserListResponse] = []
    users_query: list[User] = session.query(User).limit(10).all()
    for user in users_query:
        users.append(UserListResponse(username=user.username, first_name=user.first_name))
    return users
