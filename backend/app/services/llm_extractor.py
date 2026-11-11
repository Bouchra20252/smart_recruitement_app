import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai

from app.schemas.candidate import CandidateProfile


# Load environment variables
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")


# Initialize Gemini client
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)


async def extract_candidate_profile_with_ai(cv_text: str):

    interaction = await client.aio.interactions.create(
        model="gemini-3.8-flash",

        input=f"""
        You are an expert CV information extraction assistant.

        Analyze the following CV and extract its information.

        Rules:
        - Extract only information explicitly present in the CV.
        - Never invent or assume missing information.
        - Identify the candidate's actual name using context.
        - Group each professional experience into one entry.
        - Keep education qualifications as separate entries.
        - Do not confuse academic projects with professional experience.
        - Extract only explicitly mentioned technical skills.
        - Keep certifications separate from skills.
        - Extract each language and its proficiency separately.
        - If information is unavailable, use null or an empty list.

        CV CONTENT:

        {cv_text}
        """,

        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": CandidateProfile.model_json_schema()
        }
    )

    candidate = CandidateProfile.model_validate_json(
        interaction.output_text
    )

    return candidate