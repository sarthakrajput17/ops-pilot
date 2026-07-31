from fastapi import APIRouter, UploadFile, File, Form

from app.services.docker_service import DockerService

router = APIRouter(
    prefix="/docker",
    tags=["Docker"],
)

service = DockerService()


@router.post("/analyze")
async def analyze_dockerfile(
    dockerfile: UploadFile = File(...),
    question: str = Form("Analyze this Dockerfile."),
):

    content = (await dockerfile.read()).decode("utf-8")

    return service.analyze(
        question=question,
        content=content,
    )