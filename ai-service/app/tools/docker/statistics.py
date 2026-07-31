from app.models.docker_models import DockerStatistics


class DockerStatisticsCalculator:

    @staticmethod
    def calculate(findings):

        stats = DockerStatistics()

        for finding in findings:

            severity = finding.severity.lower()

            if severity == "critical":
                stats.critical += 1

            elif severity == "high":
                stats.high += 1

            elif severity == "medium":
                stats.medium += 1

            elif severity == "low":
                stats.low += 1

        return stats