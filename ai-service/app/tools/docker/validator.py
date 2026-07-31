from app.models.finding import Finding


class DockerValidator:

    @staticmethod
    def validate(lines):

        findings = []

        for line in lines:

            if line.startswith("FROM") and ":latest" in line:

                findings.append(
                    Finding(
                        category="docker",
                        rule_id="DOCKER-001",
                        severity="MEDIUM",
                        title="Mutable Base Image",
                        description="Docker image uses latest tag.",
                        recommendation="Pin image to a specific version.",
                    )
                )

        return findings