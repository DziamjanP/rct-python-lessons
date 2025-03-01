from typing import Optional
from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import datetime

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[Optional[str]]
    completed: Mapped[bool] = mapped_column(default=False)
    deadline: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(timezone=False))

    def __repr__(self) -> str:
        return f"Task(id={self.id!r}, title={self.title!r}, description={self.description!r}, completed={self.completed!r}, deadline={self.deadline!r})"

    