from fastapi import APIRouter, HTTPException
from app.models.result_model import EvaluationRequest, EvaluationResult
from app.services.evaluator import evaluate_mcq

eval_router = APIRouter()

@eval_router.post("/evaluate", response_model=EvaluationResult)
async def evaluate(answers: EvaluationRequest):
    user_answers = [answer.user_answer for answer in answers.answers]
    correct_answers = ["correct answer 1", "correct answer 2"]  # Placeholder

    if len(user_answers) != len(correct_answers):
        raise HTTPException(status_code=400, detail="Mismatch in answer counts.")

    result = evaluate_mcq(user_answers, correct_answers)
    return result
