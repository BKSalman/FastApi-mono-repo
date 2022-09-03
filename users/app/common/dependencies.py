import json
from users.app.api.users.schemas import UserResponse
from users.app.common.db import db
from users.app.common.exceptions import InvalidCredentialsException, NoTokenException
from users.app.config import config
from commons.dependencies import get_db_session_dependency, get_redis_dependency
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

get_db_read_session = get_db_session_dependency(db.ReadSessionLocal)
db_read_session = Depends(get_db_read_session)

get_db_session = get_db_session_dependency(db.SessionLocal)
db_session = Depends(get_db_session)

get_redis_client = get_redis_dependency(config=config)
redis_client = Depends(get_redis_client)


def get_verified_current_user(
    token: str | None = Depends(OAuth2PasswordBearer(tokenUrl="users/login", auto_error=False)),
) -> UserResponse:
    if token is None:
        raise NoTokenException()

    try:
        payload = jwt.decode(token, config.AUTH_JWT_KEY, algorithms=[config.ALGORITHM])
    except JWTError:
        raise InvalidCredentialsException()

    user = payload.get("sub")
    if user is None:
        raise InvalidCredentialsException()
    user = user.replace("'", '"')
    user = json.loads(user)
    return UserResponse(id=user["id"], username=user["username"], first_name=user["first_name"])
