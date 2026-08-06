from app.tools.core.file_detector import FileDetector, FileType

from app.services.kubernetes_service import KubernetesService
from app.services.docker_service import DockerService
from app.services.terraform_service import TerraformService


class UniversalAnalysisService:

    def __init__(self):
        self.kubernetes = KubernetesService()
        self.docker = DockerService()
        self.terraform = TerraformService()

    def analyze(
        self,
        filename: str,
        content: str,
        question: str,
    ):

        file_type = FileDetector.detect(
            filename=filename,
            content=content,
        )

        if file_type == FileType.KUBERNETES:
            result = self.kubernetes.analyze(
                question=question,
                content=content,
            )

        elif file_type == FileType.DOCKER:
            result = self.docker.analyze(
                question=question,
                content=content,
            )

        elif file_type == FileType.TERRAFORM:
            result = self.terraform.analyze(
                question=question,
                content=content,
            )

        else:
            raise ValueError("Unsupported file type.")

        # Optional metadata for the UI
        result.tool = file_type.value

        return result