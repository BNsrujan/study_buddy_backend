from transformers import pipeline

summarizer = pipeline("summarization")

def generate_summary(text: str) -> str:
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
