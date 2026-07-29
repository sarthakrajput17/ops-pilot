from pydantic import BaseModel

from app.models.finding import Finding


class KubernetesStatistics(BaseModel):
    critical: int = 0
    high: int = 0
    medium: int = 0
    low: int = 0


class KubernetesAnalysis(BaseModel):

    summary: str

    issues: list[str]

    security: list[str]

    recommendations: list[str]

    validation_issues: list[Finding] = []

    score: int = 100

    grade: str = "A"

    risk: str = "LOW"

    statistics: KubernetesStatistics = KubernetesStatistics()