from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.base import Base

class NoteORM(Base):
    __tablename__ = "notes"

    id:           Mapped[int]      = mapped_column(Integer, primary_key=True)
    user_id:      Mapped[int]      = mapped_column(Integer, ForeignKey("users.id"))
    title:        Mapped[str]      = mapped_column(String(255), nullable=False)
    body:         Mapped[str]      = mapped_column(Text, default="")
    created_at:   Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at:   Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    user: Mapped["UserORM"] = relationship(back_populates="notes")