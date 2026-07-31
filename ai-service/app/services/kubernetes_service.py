from app.services.base_analysis_service import BaseAnalysisService

from app.llm.prompts.kubernetes_prompts import KubernetesPrompts

from app.tools.kubernetes.manifest_parser import ManifestParser
from app.tools.kubernetes.validators import KubernetesValidator


class KubernetesService(BaseAnalysisService):

    def scan(self, manifest):

        parsed = ManifestParser.parse(manifest)

        return KubernetesValidator.validate(parsed)

    def build_prompt(
        self,
        question,
        manifest,
        findings,
        score,
    ):

        return KubernetesPrompts.explain_manifest(
            question=question,
            manifest=manifest,
            findings=findings,
            score=score,
        )