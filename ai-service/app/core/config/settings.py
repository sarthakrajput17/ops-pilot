from dotenv import load_dotenv
import os

load_dotenv()


class Settings:

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
    LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash")
    LLM_API_KEY = os.getenv("LLM_API_KEY")


settings = Settings()