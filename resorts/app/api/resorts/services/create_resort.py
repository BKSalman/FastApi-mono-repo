from sqlalchemy.orm import Session
from resorts.app.api.resorts.models import Resort

from resorts.app.api.resorts.schemas import ResortCreateRequest, ResortResponse


def create_resort_(
    current_user: dict,
    request_resort: ResortCreateRequest,
    session: Session,
):
    resort: Resort = Resort(
        name=request_resort.name,
        user_id=current_user["sub"]["id"],
    )

    session.add(resort)
    session.commit()

    return ResortResponse(id=resort.id, name=resort.name)
