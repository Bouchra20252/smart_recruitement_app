import re

from app.schemas.candidate import CandidateProfile


TECHNICAL_SKILLS = [
    "Python", "Java", "C++", "C#", "SQL",
    "Machine Learning", "Deep Learning",
    "TensorFlow", "PyTorch", "Scikit-learn",
    "NLP", "Pandas", "NumPy",
    "React", "Django", "FastAPI",
    "Docker", "Git", "MongoDB",
    "MySQL", "Oracle", "Hadoop",
    "Spark", "AWS", "Azure",
    "Node.js", "JavaScript", "HTML", "CSS"
]


def extract_section(text, start, end=None):

    pattern = rf"{start}\s*\n(.*?)(?=\n{end}\s*\n|\Z)"

    match = re.search(
        pattern,
        text,
        re.IGNORECASE | re.DOTALL
    )

    if match:
        return match.group(1).strip()

    return ""


def extract_candidate_profile(text: str) -> CandidateProfile:

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # Personal information
    email_match = re.search(
        r'[\w.+-]+@[\w-]+\.[\w.-]+',
        text
    )

    phone_match = re.search(
        r'\+?\d[\d\s().-]{7,}\d',
        text
    )

    full_name = lines[0] if lines else None

    # Location
    location_match = re.search(
        r'Casablanca,\s*Morocco',
        text,
        re.IGNORECASE
    )

    # Extract CV sections
    summary = extract_section(
        text, "PROFILE", "EDUCATION"
    )

    education_text = extract_section(
        text, "EDUCATION", "PROFESSIONAL EXPERIENCE"
    )

    experience_text = extract_section(
        text, "PROFESSIONAL EXPERIENCE", "ACADEMIC PROJECTS"
    )

    certifications_text = extract_section(
        text, "CERTIFICATIONS", "LANGUAGES & INTERESTS"
    )

    languages_text = extract_section(
        text, "LANGUAGES & INTERESTS"
    )

    # Extract technical skills
    text_lower = text.lower()

    technical_skills = [
        skill for skill in TECHNICAL_SKILLS
        if skill.lower() in text_lower
    ]

    # Convert sections into lists
    education = [
        line for line in education_text.splitlines()
        if line.strip()
    ]

    experience = [
        line for line in experience_text.splitlines()
        if line.strip()
    ]

    certifications = [
        item.strip()
        for item in certifications_text.split("|")
        if item.strip()
    ]

    languages = []

    if languages_text:
        language_match = re.search(
            r'Languages:\s*(.*?)(?:\n|$)',
            languages_text,
            re.IGNORECASE
        )

        if language_match:
            languages = [
                item.strip()
                for item in language_match.group(1).split(",")
            ]

    return CandidateProfile(
        full_name=full_name,
        email=email_match.group(0) if email_match else None,
        phone=phone_match.group(0).strip() if phone_match else None,
        location=location_match.group(0) if location_match else None,
        summary=summary,
        education=education,
        experience=experience,
        technical_skills=technical_skills,
        certifications=certifications,
        languages=languages
    )