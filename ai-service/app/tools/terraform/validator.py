from app.models.finding import Finding


class TerraformValidator:

    @staticmethod
    def validate(lines):

        findings = []

        text = "\n".join(lines)

        # ---------------------------------
        # TF-001
        # Open Security Group
        # ---------------------------------

        if "0.0.0.0/0" in text:

            findings.append(
                Finding(
                    category="terraform",
                    rule_id="TF-001",
                    severity="HIGH",
                    title="Open Security Group",
                    description="Security group allows ingress from anywhere.",
                    recommendation="Restrict CIDR ranges to trusted IPs.",
                )
            )

        # ---------------------------------
        # TF-002
        # Provider Version Missing
        # ---------------------------------

        if 'required_providers' in text and 'version' not in text:

            findings.append(
                Finding(
                    category="terraform",
                    rule_id="TF-002",
                    severity="MEDIUM",
                    title="Provider Version Missing",
                    description="Terraform provider version is not pinned.",
                    recommendation="Specify an explicit provider version.",
                )
            )

        # ---------------------------------
        # TF-003
        # Missing Tags
        # ---------------------------------

        if "resource" in text and "tags" not in text:

            findings.append(
                Finding(
                    category="terraform",
                    rule_id="TF-003",
                    severity="LOW",
                    title="Missing Resource Tags",
                    description="Resources should include tags.",
                    recommendation="Add tags for ownership, environment, and cost tracking.",
                )
            )

        return findings