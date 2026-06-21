from sqlalchemy import Integer, String, SmallInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.base import Base

class TaskORM(Base):
    __tablename__ = "tasks"

    id:           Mapped[int]      = mapped_column(Integer, primary_key=True)
    user_id:      Mapped[int]      = mapped_column(Integer, ForeignKey("users.id"))
    title:        Mapped[str]      = mapped_column(String(255), nullable=False)
    description:  Mapped[str]      = mapped_column(Text, default="No description")
    priority:     Mapped[int]      = mapped_column(SmallInteger, default=0)
    status:       Mapped[int]      = mapped_column(SmallInteger, default=0)
    due_date:     Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at:   Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    completed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    user: Mapped["UserORM"] = relationship(back_populates="tasks")