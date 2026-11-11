from pydantic import BaseModel, Field
from typing import Optional


class Education(BaseModel):
    degree: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None


class Experience(BaseModel):
    position: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    description: list[str] = Field(default_factory=list)


class CandidateProfile(BaseModel):

    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None

    summary: Optional[str] = None

    education: list[Education] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    

    technical_skills: list[str] = Field(default_factory=list)
    soft_skills: list[str] = Field(default_factory=list)

    certifications: list[str] = Field(default_factory=list)
    languages: list[str] = Field(default_factory=list)
   