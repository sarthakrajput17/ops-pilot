from app.models.skill_type import SkillType


class AIRouter:

    def route(self, message: str) -> SkillType:

        text = message.lower()

        kubernetes_keywords = [
            "pod",
            "deployment",
            "service",
            "namespace",
            "kubectl",
            "ingress",
            "configmap",
            "secret"
        ]

        docker_keywords = [
            "docker",
            "dockerfile",
            "container",
            "image",
            "compose"
        ]

        terraform_keywords = [
            "terraform",
            "tf",
            "aws",
            "resource"
        ]

        github_keywords = [
            "github",
            "workflow",
            "actions",
            "ci",
            "pipeline"
        ]

        if any(word in text for word in kubernetes_keywords):
            return SkillType.KUBERNETES

        if any(word in text for word in docker_keywords):
            return SkillType.DOCKER

        if any(word in text for word in terraform_keywords):
            return SkillType.TERRAFORM

        if any(word in text for word in github_keywords):
            return SkillType.GITHUB

        return SkillType.GENERAL