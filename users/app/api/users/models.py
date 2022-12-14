from datetime import datetime
from sqlalchemy.orm import relationship, Mapped
import sqlalchemy as sa
from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.String, primary_key=True, default=generate_random_uuid)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    resorts: Mapped[str] = relationship("Resort")

    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)
    username = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=True)
    nationality = sa.Column(sa.String, nullable=True)
    bio = sa.Column(sa.String, nullable=True)
    password = sa.Column(sa.String, nullable=False)
