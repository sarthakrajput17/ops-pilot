import yaml


class ManifestParser:

    @staticmethod
    def parse(manifest: str) -> dict:
        """
        Parse Kubernetes YAML into a Python dictionary.
        """

        return yaml.safe_load(manifest)

    @staticmethod
    def get_kind(manifest: str) -> str:
        """
        Return the Kubernetes resource kind.
        """

        data = yaml.safe_load(manifest)

        return data.get("kind", "Unknown")