from pydantic import BaseModel


class DockerStatistics(BaseModel):
    critical: int = 0
    high: int = 0
    medium: int = 0
    low: int = 0


class DockerAnalysis(BaseModel):

    summary: str

    issues: list[str]

    recommendations: list[str]

    score: int = 100

    grade: str = "A"

    risk: str = "LOW"

    statistics: DockerStatistics = DockerStatistics()

    validation_issues: list = []