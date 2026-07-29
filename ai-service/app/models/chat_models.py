from typing import Optional

from pydantic import BaseModel

from app.models.kubernetes_models import KubernetesAnalysis


class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None


class ChatResponse(BaseModel):
    response: str | KubernetesAnalysis