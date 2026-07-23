from app.llm.router.ai_router import AIRouter
from app.skills.skill_registry import SkillRegistry


class AIOrchestrator:

    def __init__(self):

        self.router = AIRouter()

        self.registry = SkillRegistry()

    def process(self, message: str):

        skill_type = self.router.route(message)

        skill = self.registry.get(skill_type)

        response = skill.execute(message)

        return response