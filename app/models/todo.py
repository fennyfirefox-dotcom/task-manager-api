from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from app.database import Base


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(Text)
    is_done: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))