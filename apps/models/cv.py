from datetime import datetime
from sqlalchemy import BigInteger, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class CV(Base):
    __tablename__ = "cvs"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(200))
    speciality: Mapped[str] = mapped_column(String(200))
    experiences: Mapped[str] = mapped_column(Text)
    skills: Mapped[str] = mapped_column(Text)
    projects: Mapped[str] = mapped_column(Text)
    cv_text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)