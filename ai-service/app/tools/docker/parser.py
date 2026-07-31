class DockerParser:

    @staticmethod
    def parse(content: str):

        instructions = []

        for line in content.splitlines():

            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            instructions.append(line)

        return instructions