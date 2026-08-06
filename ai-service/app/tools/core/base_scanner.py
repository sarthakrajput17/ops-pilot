from abc import ABC, abstractmethod


class BaseScanner(ABC):
    """
    Base class for every scanner.
    """

    @abstractmethod
    def parse(self, content):
        pass

    @abstractmethod
    def validate(self, parsed):
        pass

    def scan(self, content):
        """
        Generic scan pipeline.

        Parse
            ↓
        Validate
            ↓
        Return Findings
        """

        parsed = self.parse(content)

        findings = self.validate(parsed)

        return findings