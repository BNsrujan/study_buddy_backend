from transformers import pipeline

qa_pipeline = pipeline("question-generation")

def create_mcqs(text: str) -> list:
    questions = qa_pipeline(text)
    mcqs = []
    for qa in questions:
        question = qa["question"]
        answer = qa["answer"]
        # Create dummy options for demonstration purposes
        mcqs.append({
            "question": question,
            "options": [answer, "Option B", "Option C", "Option D"],
            "answer": answer
        })
    return mcqs
