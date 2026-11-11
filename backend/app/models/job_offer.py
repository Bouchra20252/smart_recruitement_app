from sqlalchemy import String, Integer, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class JobOffer(Base):

    __tablename__ = "job_offers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    company: Mapped[str] = mapped_column(String(255), nullable=False)
    location: Mapped[str | None] = mapped_column(String(150))

    description: Mapped[str | None] = mapped_column(Text)

    required_skills: Mapped[list] = mapped_column(JSON, default=list)
    preferred_skills: Mapped[list] = mapped_column(JSON, default=list)

    experience_level: Mapped[str | None] = mapped_column(String(100))
    contract_type: Mapped[str | None] = mapped_column(String(100))

    application_url: Mapped[str | None] = mapped_column(String(500))