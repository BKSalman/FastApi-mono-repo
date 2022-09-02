from resorts.app.common.dependencies import db_session
from fastapi import APIRouter
from sqlalchemy.orm import Session

from .schemas import ResortResponse
from .services.list_resorts import list_resorts_

resorts_router = APIRouter(prefix="/resorts", tags=["resorts"])


@resorts_router.get(
    path="",
    response_model=list[ResortResponse],
)
def list_resorts(
    session: Session = db_session,
):
    return list_resorts_(session=session)
