from fastapi import APIRouter, HTTPException
from app.models.summary_model import SummaryResponse
from app.services.summarizer import summarize_text

summary_router = APIRouter()

@summary_router.post("/summarize", response_model=SummaryResponse)
async def get_summary(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="Text is required.")
    summary = summarize_text(text)
    return {"summary_text": summary}
