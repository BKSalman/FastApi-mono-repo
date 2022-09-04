from sqlalchemy import select
from sqlalchemy.orm import Session
from commons.schemas import UserResponse
from resorts.app.api.resorts.models import Resort


def list_resorts_(
    session: Session,
    current_user: UserResponse,
) -> list:
    stmt = select(Resort).where(Resort.user_id == current_user.id).order_by(Resort.created.desc())
    resorts: list[Resort] = session.execute(stmt).scalars().all()
    return resorts
