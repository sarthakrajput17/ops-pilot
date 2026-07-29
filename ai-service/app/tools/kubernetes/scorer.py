class KubernetesScorer:

    SEVERITY_SCORES = {
        "LOW": 3,
        "MEDIUM": 7,
        "HIGH": 15,
        "CRITICAL": 25,
    }

    @staticmethod
    def calculate(findings):

        score = 100

        for finding in findings:
            score -= KubernetesScorer.SEVERITY_SCORES.get(
                finding.severity.upper(),
                5,
            )

        return max(score, 0)