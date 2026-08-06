class DockerScorer:

    @staticmethod
    def calculate(findings):

        score = 100

        for finding in findings:

            if finding.severity == "CRITICAL":
                score -= 30

            elif finding.severity == "HIGH":
                score -= 20

            elif finding.severity == "MEDIUM":
                score -= 10

            elif finding.severity == "LOW":
                score -= 5

        return max(score, 0)