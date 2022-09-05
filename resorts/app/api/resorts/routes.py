from resorts.app.api.resorts.services.create_resort import create_resort_
from resorts.app.common.dependencies import db_session
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from resorts.app.api.resorts.models import Resort
from commons.schemas import UserResponse
from resorts.app.common.utils import get_verified_current_user

# from .schemas import
from commons.schemas import UserToken
from .schemas import ResortCreateRequest, ResortResponse
from .services.list_resorts import list_resorts_

resorts_router = APIRouter(prefix="/resorts", tags=["resorts"])


@resorts_router.get(
    path="",
    # response_model=list[ResortResponse],
)
def list_resorts(
    session: Session = db_session,
    current_user: UserResponse = Depends(get_verified_current_user),
):
    return list_resorts_(current_user=current_user, session=session)


# @resorts_router.post("", response_model=ResortResponse)
# def create_resort(
#     request_resort: ResortCreateRequest,
#     session: Session = db_session,
# ):
#     return create_resort_(request_resort, session)


# @resorts_router.get("/me")
# def read_current_user(
#     current_user: UserResponse = Depends(get_verified_current_user),
#     session: Session = db_session,
#     # response_model=UserResponse,  # there is a weird error when using this
# ):
#     user: User | None = session.query(User).filter_by(id=current_user.id).first()
#     if user is None:
#         raise InvalidCredentialsException()
#     return UserResponse(
#         id=user.id,
#         username=user.username,
#         email=user.email,
#         first_name=user.first_name,
#         last_name=user.last_name,
#         nationality=user.nationality,
#         bio=user.bio,
#     )


# @resorts_router.patch("")
# def update_user(
#     request_user_updates: UserUpdateRequest,
#     current_user: UserResponse = Depends(get_verified_current_user),
#     session: Session = db_session,
# ):
#     return update_user_(request_user_updates, current_user, session)
