import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.core.database.base import Base


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )
