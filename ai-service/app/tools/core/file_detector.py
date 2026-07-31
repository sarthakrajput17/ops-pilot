from enum import Enum


class FileType(str, Enum):
    KUBERNETES = "kubernetes"
    DOCKER = "docker"
    TERRAFORM = "terraform"
    UNKNOWN = "unknown"


class FileDetector:

    @staticmethod
    def detect(filename: str, content: str) -> FileType:

        filename = filename.lower()

        if filename == "dockerfile":
            return FileType.DOCKER

        if filename.endswith(".tf"):
            return FileType.TERRAFORM

        if "apiVersion:" in content and "kind:" in content:
            return FileType.KUBERNETES

        return FileType.UNKNOWN