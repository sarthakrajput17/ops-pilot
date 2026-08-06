class KubernetesPrompts:

    @staticmethod
    def explain_manifest(
        question: str,
        manifest: str,
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
You are a Senior Kubernetes Platform Engineer with expertise in production-grade Kubernetes deployments.

Your job is NOT to rediscover problems.

The local validation engine has already analyzed the manifest.

Use those findings to explain WHY they matter and HOW to fix them.

--------------------------------------------------

Question

{question}

--------------------------------------------------

Production Readiness Score

{score}/100

--------------------------------------------------

Validator Findings

{findings_text}

--------------------------------------------------

Deployment Manifest

{manifest}

--------------------------------------------------

Instructions

1. Explain the deployment briefly.

2. Explain every validation finding.

3. Explain the production risks.

4. Suggest best-practice improvements.

5. Mention any additional observations that are NOT already covered by the validator.

Return ONLY valid JSON.

Required JSON schema:

{{
    "summary": "...",

    "issues":[...],

    "security":[...],

    "recommendations":[...]
}}

Do not return markdown.

Do not return code fences.

Return JSON only.
--------------------------------------------------

You MUST return a structured response.

Additionally, generate a production-ready corrected Kubernetes manifest.

Rules:

- Fix every validation issue.
- Add missing Kubernetes best practices.
- Preserve the application's behaviour.
- Do NOT remove resources.
- Return the complete corrected YAML.

Store the corrected YAML in the field:

fixed_manifest
"""