from fastapi import APIRouter, UploadFile, File, Form

from app.services.universal_service import UniversalAnalysisService

router = APIRouter(
    tags=["Universal Analysis"],
)


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    question: str = Form(...),
):
    content = (await file.read()).decode("utf-8")

    service = UniversalAnalysisService()

    return service.analyze(
        filename=file.filename,
        content=content,
        question=question,
    )