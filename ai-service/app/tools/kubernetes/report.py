class KubernetesReport:

    @staticmethod
    def build(
        score: int,
        findings,
        statistics,
    ):

        if score >= 90:
            grade = "A"
            risk = "LOW"

        elif score >= 75:
            grade = "B"
            risk = "LOW"

        elif score >= 60:
            grade = "C"
            risk = "MEDIUM"

        elif score >= 40:
            grade = "D"
            risk = "HIGH"

        else:
            grade = "F"
            risk = "CRITICAL"

        return {
            "score": score,
            "grade": grade,
            "risk": risk,
            "statistics": statistics,
            "findings": findings,
        }