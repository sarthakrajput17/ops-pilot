from app.services.base_analysis_service import BaseAnalysisService

from app.llm.prompts.docker_prompts import DockerPrompts

from app.tools.docker.scanner import DockerScanner


class DockerService(BaseAnalysisService):

    def scan(self, dockerfile):

        return DockerScanner.scan(dockerfile)

    def build_prompt(
        self,
        question,
        dockerfile,
        findings,
        score,
    ):

        return DockerPrompts.explain_dockerfile(
            question=question,
            dockerfile=dockerfile,
            findings=findings,
            score=score,
        )