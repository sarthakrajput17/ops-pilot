from app.tools.core.base_scanner import BaseScanner
from app.tools.docker.parser import DockerParser
from app.tools.docker.validator import DockerValidator


class DockerScanner(BaseScanner):

    @staticmethod
    def scan(content: str):

        lines = DockerParser.parse(content)

        findings = DockerValidator.validate(lines)

        return findings 