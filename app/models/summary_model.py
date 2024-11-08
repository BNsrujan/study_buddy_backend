from pydantic import BaseModel

class PDFUpload(BaseModel):
    file_path: str

class SummaryResponse(BaseModel):
    summary_text: str
