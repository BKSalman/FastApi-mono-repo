from sqlalchemy.orm import Session
from resorts.app.api.resorts.models import Resort


def list_resorts_(session: Session) -> list:
    return session.query(Resort).limit(10).all()
