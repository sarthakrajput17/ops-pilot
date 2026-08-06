class DockerReport:

    @staticmethod
    def build(score, findings, statistics):

        if score >= 90:
            grade = "A"

        elif score >= 75:
            grade = "B"

        elif score >= 60:
            grade = "C"

        elif score >= 40:
            grade = "D"

        else:
            grade = "F"

        if score >= 80:
            risk = "LOW"

        elif score >= 60:
            risk = "MEDIUM"

        else:
            risk = "HIGH"

        return {
            "score": score,
            "grade": grade,
            "risk": risk,
            "findings": findings,
            "statistics": statistics,
        }