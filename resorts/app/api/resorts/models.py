from datetime import datetime

import sqlalchemy as sa
from commons.db import Base
from commons.utils.generate_random_id_uuid import generate_random_uuid


class Resort(Base):
    __tablename__ = "resorts"

    id = sa.Column(sa.String, primary_key=True, default=generate_random_uuid)
    created = sa.Column(sa.DateTime, default=datetime.now, nullable=False)
    updated = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    name = sa.Column(sa.String, nullable=True)
