from app.services.kubernetes_service import KubernetesService


class KubernetesSkill:

    def __init__(self):
        self.service = KubernetesService()

    def execute(
        self,
        message: str,
        context: str | None = None,
    ):

        if not context:
            return "Please provide a Kubernetes manifest."

        return self.service.analyze(
            question=message,
            manifest=context,
        )