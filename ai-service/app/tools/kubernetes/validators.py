from app.tools.kubernetes.rules import (
    LOW_REPLICAS,
    LATEST_IMAGE_TAG,
    MISSING_RESOURCES,
    MISSING_LIVENESS,
    MISSING_READINESS,
    MISSING_STARTUP,
    MISSING_SECURITY_CONTEXT,
)


class KubernetesValidator:

    @staticmethod
    def validate(manifest):

        findings = []

        if manifest.get("kind") != "Deployment":
            return findings

        spec = manifest.get("spec", {})
        template = spec.get("template", {})
        pod_spec = template.get("spec", {})

        containers = pod_spec.get("containers", [])

        replicas = spec.get("replicas", 1)

        # Replica validation
        if replicas < 2:
            findings.append(
                LOW_REPLICAS.build(
                    "Deployment has only one replica."
                )
            )

        for container in containers:

            name = container.get("name", "unknown")
            image = container.get("image", "")

            # Latest image tag
            if image.endswith(":latest"):
                findings.append(
                    LATEST_IMAGE_TAG.build(
                        f"Container '{name}' is using the latest image tag."
                    )
                )

            # Resource limits
            resources = container.get("resources")

            if not resources:
                findings.append(
                    MISSING_RESOURCES.build(
                        f"Container '{name}' has no resource requests or limits."
                    )
                )

            # Liveness Probe
            if "livenessProbe" not in container:
                findings.append(
                    MISSING_LIVENESS.build(
                        f"Container '{name}' is missing a liveness probe."
                    )
                )

            # Readiness Probe
            if "readinessProbe" not in container:
                findings.append(
                    MISSING_READINESS.build(
                        f"Container '{name}' is missing a readiness probe."
                    )
                )

            # Startup Probe
            if "startupProbe" not in container:
                findings.append(
                    MISSING_STARTUP.build(
                        f"Container '{name}' is missing a startup probe."
                    )
                )

            # Security Context
            if "securityContext" not in container:
                findings.append(
                    MISSING_SECURITY_CONTEXT.build(
                        f"Container '{name}' has no security context."
                    )
                )

        return findings