from pydantic import BaseModel


class Finding(BaseModel):

    rule_id: str

    severity: str

    category: str

    title: str

    description: str

    recommendation: str