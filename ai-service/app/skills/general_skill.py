from app.llm.factory.llm_factory import LLMFactory


class GeneralSkill:

    def __init__(self):

        self.provider = LLMFactory.create()

    def execute(self, message: str):

        return self.provider.generate(message)