from fastapi import APIRouter, HTTPException
from app.models.mcq_model import MCQResponse
from app.services.mcq_generator import generate_mcqs

mcq_router = APIRouter()

@mcq_router.post("/generate_mcqs", response_model=MCQResponse)
async def generate_mcq(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required.")
    mcqs = generate_mcqs(text)
    return {"mcqs": mcqs}
