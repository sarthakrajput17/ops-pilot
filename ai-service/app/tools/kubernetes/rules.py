from app.models.finding import Finding


class KubernetesRule:

    def __init__(
        self,
        rule_id: str,
        severity: str,
        category: str,
        title: str,
        recommendation: str,
    ):
        self.rule_id = rule_id
        self.severity = severity
        self.category = category
        self.title = title
        self.recommendation = recommendation

    def build(self, description: str) -> Finding:
        return Finding(
            rule_id=self.rule_id,
            severity=self.severity,
            category=self.category,
            title=self.title,
            description=description,
            recommendation=self.recommendation,
        )

MISSING_SECURITY_CONTEXT = KubernetesRule(
    rule_id="K8S-001",
    severity="HIGH",
    category="Security",
    title="Missing Security Context",
    recommendation=(
        "Configure securityContext with runAsNonRoot, "
        "readOnlyRootFilesystem and drop unnecessary capabilities."
    ),
)

LATEST_IMAGE_TAG = KubernetesRule(
    rule_id="K8S-002",
    severity="MEDIUM",
    category="Deployment",
    title="Mutable Image Tag",
    recommendation="Pin the image to a specific version or SHA digest.",
)

MISSING_RESOURCES = KubernetesRule(
    rule_id="K8S-003",
    severity="HIGH",
    category="Performance",
    title="Missing Resource Limits",
    recommendation="Configure CPU and memory requests and limits.",
)

MISSING_LIVENESS = KubernetesRule(
    rule_id="K8S-004",
    severity="MEDIUM",
    category="Reliability",
    title="Missing Liveness Probe",
    recommendation="Add a livenessProbe.",
)

MISSING_READINESS = KubernetesRule(
    rule_id="K8S-005",
    severity="MEDIUM",
    category="Reliability",
    title="Missing Readiness Probe",
    recommendation="Add a readinessProbe.",
)

MISSING_STARTUP = KubernetesRule(
    rule_id="K8S-006",
    severity="LOW",
    category="Reliability",
    title="Missing Startup Probe",
    recommendation="Add a startupProbe.",
)

LOW_REPLICAS = KubernetesRule(
    rule_id="K8S-007",
    severity="MEDIUM",
    category="Availability",
    title="Low Replica Count",
    recommendation="Run at least two replicas in production.",
)    