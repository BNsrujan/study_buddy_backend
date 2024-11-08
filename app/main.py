from fastapi import FastAPI, UploadFile, File
from app.services import pdf_converter, summarizer, keypoints_generator, mcq_generator, evaluator

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Step 1: Convert PDF to text
    content = await file.read()
    text = pdf_converter.convert_pdf_to_text(content)
    
    # Step 2: Summarize the text
    summary = summarizer.generate_summary(text)
    
    # Step 3: Extract key points
    keypoints = keypoints_generator.extract_key_points(summary)
    
    # Step 4: Generate MCQ questions
    questions = mcq_generator.create_mcqs(summary)

    return {
        "summary": summary,
        "key_points": keypoints,
        "questions": questions
    }

@app.post("/evaluate/")
async def evaluate_answers(answers: dict):
    # Step 5: Evaluate the answers
    result = evaluator.evaluate(answers)
    return {"evaluation": result}
