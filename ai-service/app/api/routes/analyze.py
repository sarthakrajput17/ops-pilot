from fastapi import APIRouter, Request, UploadFile, File, Form
from fastapi.templating import Jinja2Templates
from app.api.routes.pdf import latest_analysis
import app.api.routes.pdf as pdf_route

from app.services.universal_service import UniversalAnalysisService

router = APIRouter(
    tags=["Universal Analysis"],
)

templates = Jinja2Templates(directory="templates")


@router.post("/analyze")
async def analyze(
    request: Request,
    file: UploadFile = File(...),
    question: str = Form(...),
):

    content = (await file.read()).decode("utf-8")

    service = UniversalAnalysisService()

    analysis = service.analyze(
        filename=file.filename,
        content=content,
        question=question,
    )

    pdf_route.latest_analysis = analysis

    return templates.TemplateResponse(
        request=request,
        name="report.html",
        context={
            "request": request,
            "analysis": analysis,
        },
    )