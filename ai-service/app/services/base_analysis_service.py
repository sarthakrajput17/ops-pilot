from abc import ABC, abstractmethod

from app.llm.factory.llm_factory import LLMFactory
from app.models.devops_models import DevOpsAnalysis

from app.tools.core.scoring import ScoringEngine
from app.tools.core.statistics import StatisticsEngine
from app.tools.core.report_builder import ReportBuilder


class BaseAnalysisService(ABC):

    def __init__(self):
        self.provider = LLMFactory.create()

    @abstractmethod
    def scan(self, content):
        """
        Child service returns findings.
        """
        pass

    @abstractmethod
    def build_prompt(
        self,
        question,
        content,
        findings,
        score,
    ):
        """
        Child service builds LLM prompt.
        """
        pass

    def analyze(
        self,
        question,
        content,
    ) -> DevOpsAnalysis:

        # Scan
        findings = self.scan(content)

        # Score
        score = ScoringEngine.calculate(findings)

        # Statistics
        statistics = StatisticsEngine.calculate(findings)

        # Report
        report = ReportBuilder.build(
            score=score,
            findings=findings,
            statistics=statistics,
        )

        # Prompt
        prompt = self.build_prompt(
            question,
            content,
            findings,
            score,
        )

        try:

            analysis = self.provider.generate_structured(
                prompt,
                DevOpsAnalysis,
            )

        except Exception as e:

            print(e)

            analysis = DevOpsAnalysis(
                summary="AI analysis is temporarily unavailable.",
                issues=[],
                security=[],
                recommendations=[],
            )

        analysis.validation_issues = report["findings"]
        analysis.score = report["score"]
        analysis.grade = report["grade"]
        analysis.risk = report["risk"]
        analysis.statistics = report["statistics"]

        return analysis