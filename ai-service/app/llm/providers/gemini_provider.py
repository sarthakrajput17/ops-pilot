from google import genai

from app.core.config.settings import settings
from app.llm.interfaces.llm_provider import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.LLM_API_KEY
        )

    def generate(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model=settings.LLM_MODEL,
            contents=prompt,
        )

        return response.text