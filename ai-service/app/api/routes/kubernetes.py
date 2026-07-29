from fastapi import APIRouter, UploadFile, File, Form

from app.services.kubernetes_service import KubernetesService

router = APIRouter(
    prefix="/kubernetes",
    tags=["Kubernetes"]
)

service = KubernetesService()


@router.post("/analyze")
async def analyze_manifest(
    message: str = Form(...),
    manifest: UploadFile = File(...)
):

    content = (await manifest.read()).decode("utf-8")

    result = service.analyze(
        question=message,
        manifest=content
    )

    return result