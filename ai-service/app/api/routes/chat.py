from fastapi import APIRouter

from app.models.chat_models import ChatRequest, ChatResponse
from app.orchestrator.ai_orchestrator import AIOrchestrator

router = APIRouter()

orchestrator = AIOrchestrator()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    response = orchestrator.process(request.message)

    return ChatResponse(response=response)