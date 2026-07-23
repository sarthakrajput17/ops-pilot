from app.core.config.settings import settings
from app.llm.providers.gemini_provider import GeminiProvider


class LLMFactory:

    @staticmethod
    def create():

        if settings.LLM_PROVIDER.lower() == "gemini":
            return GeminiProvider()

        raise ValueError(
            f"Unsupported provider: {settings.LLM_PROVIDER}"
        )