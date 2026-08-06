from collections import Counter


class StatisticsEngine:

    @staticmethod
    def calculate(findings):

        counter = Counter()

        for finding in findings:
            counter[finding.severity.upper()] += 1

        return {
            "critical": counter["CRITICAL"],
            "high": counter["HIGH"],
            "medium": counter["MEDIUM"],
            "low": counter["LOW"],
        }