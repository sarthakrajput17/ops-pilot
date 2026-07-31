class TerraformPrompts:

    @staticmethod
    def explain_terraform(
        question: str,
        terraform: str,
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
You are a Senior DevOps Engineer with expertise in Terraform and Infrastructure as Code.

Your job is NOT to rediscover problems.

The local validation engine has already analyzed the Terraform configuration.

Explain WHY the findings matter and HOW to fix them.

----------------------------------------

Question

{question}

----------------------------------------

Production Readiness Score

{score}/100

----------------------------------------

Validator Findings

{findings_text}

----------------------------------------

Terraform Configuration

{terraform}

----------------------------------------

Return JSON with:

summary

issues

security

recommendations
"""