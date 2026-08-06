from fastapi import APIRouter, UploadFile, File, Form

from app.services.terraform_service import TerraformService

router = APIRouter(
    prefix="/terraform",
    tags=["Terraform"],
)


@router.post("/analyze")
async def analyze_terraform(
    terraform: UploadFile = File(...),
    question: str = Form(...),
):

    service = TerraformService()

    content = (await terraform.read()).decode()

    return service.analyze(
        question=question,
        content=content,
    )