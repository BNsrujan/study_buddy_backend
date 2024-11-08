from fastapi import APIRouter, UploadFile, File
from app.services.pdf_processor import pdf_to_text

upload_router = APIRouter()

@upload_router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    with open(f"./uploads/{file.filename}", "wb") as f:
        f.write(content)

    text = pdf_to_text(f"./uploads/{file.filename}")
    return {"text": text}
