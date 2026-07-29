class KubernetesStatistics:

    @staticmethod
    def calculate(findings):

        stats = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
        }

        for finding in findings:

            severity = finding.severity.lower()

            if severity in stats:
                stats[severity] += 1

        return stats