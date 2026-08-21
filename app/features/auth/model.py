import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.core.database.base import Base


class Auth(Base):
    __tablename__ = "auth"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
