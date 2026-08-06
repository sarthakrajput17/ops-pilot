from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.utils.pdf_generator import generate_pdf

router = APIRouter(
    tags=["PDF"],
)

# Temporary in-memory storage
latest_analysis = None


@router.post("/download-report")
async def download_report():

    global latest_analysis

    if latest_analysis is None:
        return {"error": "No report available."}

    pdf = generate_pdf(latest_analysis)

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=ops-pilot-report.pdf"
        },
    )