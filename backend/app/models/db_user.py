from sqlalchemy import Integer, String, SmallInteger, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from app.db.base import Base

class UserORM(Base):
    __tablename__ = "users"

    id:           Mapped[int]      = mapped_column(Integer, primary_key=True)
    email:        Mapped[str]      = mapped_column(String(255), nullable=False, unique=True)
    password:     Mapped[str]      = mapped_column(String(255), nullable=False)
    frequency:    Mapped[list[int]] = mapped_column(ARRAY(Integer), default=list)
    created_at:   Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    tasks:  Mapped[list["TaskORM"]]  = relationship(back_populates="user", cascade="all, delete-orphan") # type: ignore
    notes:  Mapped[list["NoteORM"]]  = relationship(back_populates="user", cascade="all, delete-orphan") # type: ignore
    habits: Mapped[list["HabitORM"]] = relationship(back_populates="user", cascade="all, delete-orphan") # type: ignore
