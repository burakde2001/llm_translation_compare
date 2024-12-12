from pydantic import BaseModel


class Reason(BaseModel):
    quantity_score: float
    quality_score: float
    relation_score: float
    manner_score: float
    reason: str
