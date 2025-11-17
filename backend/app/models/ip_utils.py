from pydantic import BaseModel


class IPClassification(BaseModel):
    ip: str
    type: str  # "Private" or "Public"
