from app.llm.factory.llm_factory import LLMFactory
from app.llm.prompts.kubernetes_prompts import KubernetesPrompts
from app.models.kubernetes_models import KubernetesAnalysis

from app.tools.kubernetes.manifest_parser import ManifestParser
from app.tools.kubernetes.validators import KubernetesValidator
from app.tools.kubernetes.scorer import KubernetesScorer
from app.tools.kubernetes.statistics import KubernetesStatistics
from app.tools.kubernetes.report import KubernetesReport


class KubernetesService:

    def __init__(self):
        self.provider = LLMFactory.create()

    def analyze(
        self,
        question: str,
        manifest: str,
    ) -> KubernetesAnalysis:
        """
        Analyze a Kubernetes manifest using AI.
        """

        # Step 1 - Parse YAML
        manifest_dict = ManifestParser.parse(manifest)

        # Step 2 - Run local validations
        findings = KubernetesValidator.validate(manifest_dict)

        # Step 3 - Calculate production score
        score = KubernetesScorer.calculate(findings)

        # Step 4 - Calculate statistics
        statistics = KubernetesStatistics.calculate(findings)

        # Step 5 - Build production report
        report = KubernetesReport.build(
            score=score,
            findings=findings,
            statistics=statistics,
        )

        # Step 6 - Build AI prompt
        prompt = KubernetesPrompts.explain_manifest(
            question=question,
            manifest=manifest,
            findings=findings,
            score=score,
        )

        # Step 7 - Generate AI explanation
        try:
            analysis = self.provider.generate_structured(
                prompt,
                KubernetesAnalysis,
            )

        except Exception:

            analysis = KubernetesAnalysis(
                summary="AI analysis is temporarily unavailable.",
                issues=[],
                security=[],
                recommendations=[],
            )

        # Step 8 - Merge deterministic analysis
        analysis.validation_issues = report["findings"]
        analysis.score = report["score"]
        analysis.grade = report["grade"]
        analysis.risk = report["risk"]
        analysis.statistics = report["statistics"]

        return analysis