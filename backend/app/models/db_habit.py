from sqlalchemy import Integer, String, SmallInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from app.db.base import Base

class HabitORM(Base):
    __tablename__ = "habits"

    id:           Mapped[int]      = mapped_column(Integer, primary_key=True)
    user_id:      Mapped[int]      = mapped_column(Integer, ForeignKey("users.id"))
    title:        Mapped[str]      = mapped_column(String(255), nullable=False)
    frequency:    Mapped[list[int]] = mapped_column(ARRAY(Integer), default=list)
    completed_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    user: Mapped["UserORM"] = relationship(back_populates="habits") # type: ignore