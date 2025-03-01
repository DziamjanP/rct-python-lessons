from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
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

class TaskModel(BaseModel):
    id: int | None = None
    title: str = Field(max_length=256)
    description: str | None = None
    completed: bool = False
    deadline: datetime.datetime | None = None

    model_config = ConfigDict(from_attributes=True)

class TaskModelUpdate(TaskModel):
    title: str | None = Field(max_length=256, default=None)