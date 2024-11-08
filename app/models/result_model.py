from pydantic import BaseModel
from typing import List

class Answer(BaseModel):
    question: str
    user_answer: str

class EvaluationRequest(BaseModel):
    answers: List[Answer]

class EvaluationResult(BaseModel):
    score: int
    total: int
    incorrect_answers: List[str]
