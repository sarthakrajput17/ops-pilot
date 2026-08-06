from app.tools.terraform.parser import TerraformParser
from app.tools.terraform.validator import TerraformValidator


class TerraformScanner:

    @staticmethod
    def scan(terraform: str):

        parsed = TerraformParser.parse(terraform)

        findings = TerraformValidator.validate(parsed)

        return findings