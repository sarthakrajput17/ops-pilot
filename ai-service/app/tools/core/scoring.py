class ScoringEngine:
    """
    Generic scoring engine used by every scanner.
    """

    SEVERITY_POINTS = {
        "CRITICAL": 30,
        "HIGH": 20,
        "MEDIUM": 10,
        "LOW": 5,
    }

    @classmethod
    def calculate(cls, findings):

        score = 100

        for finding in findings:

            score -= cls.SEVERITY_POINTS.get(
                finding.severity.upper(),
                0,
            )

        return max(score, 0)