from app.services.base_analysis_service import BaseAnalysisService
from app.tools.terraform.scanner import TerraformScanner
from app.llm.prompts.terraform_prompts import TerraformPrompts


class TerraformService(BaseAnalysisService):

    def scan(self, content):
        return TerraformScanner.scan(content)

    def build_prompt(
        self,
        question,
        content,
        findings,
        score,
    ):
        return TerraformPrompts.explain_terraform(
            question=question,
            terraform=content,
            findings=findings,
            score=score,
        )