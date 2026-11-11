from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.llm_extractor import extract_candidate_profile_with_ai
from app.services.cv_parser import extract_text_from_pdf

router = APIRouter()


@router.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are accepted."
        )

    file_content = await file.read()

    if not file_content:
        raise HTTPException(
            status_code=400,
            detail="The uploaded file is empty."
        )

    try:
        extracted_text = extract_text_from_pdf(file_content)

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to process this PDF."
        )

    try:
        candidate = await extract_candidate_profile_with_ai(extracted_text)

    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"AI extraction failed: {str(e)}"
        )

    return {
        "filename": file.filename,
        "message": "CV analyzed successfully using AI",
        "candidate_profile": candidate.model_dump(),
        "extracted_text": extracted_text,
        "character_count": len(extracted_text)
    }