from typing import List
from pydantic import BaseModel


class ErroneousText(BaseModel):
    erroneous_text: List[str]


class GrammaticalAndSpellingCorrectnessVerdict(BaseModel):
    verdict: str
    reason: str


class Verdicts(BaseModel):
    verdicts: List[GrammaticalAndSpellingCorrectnessVerdict]


class Reason(BaseModel):
    reason: str
