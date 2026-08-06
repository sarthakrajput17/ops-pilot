class DockerPrompts:

    @staticmethod
    def explain_dockerfile(
        question: str,
        dockerfile: str,
        findings,
        score: int,
    ) -> str:

        findings_text = "\n".join(
            [
                f"- [{finding.severity}] {finding.title}: {finding.description}"
                for finding in findings
            ]
        )

        return f"""
You are a Senior DevOps Engineer with expertise in Docker and container security.

Your task is NOT to rediscover problems.

The Docker validator has already analyzed the Dockerfile.

Explain:

- why the detected issues matter
- their production impact
- how to fix them
- Docker best practices

----------------------------------------

Question

{question}

----------------------------------------

Production Score

{score}/100

----------------------------------------

Validator Findings

{findings_text}

----------------------------------------

Dockerfile

{dockerfile}

----------------------------------------

Return JSON matching the response schema.
"""