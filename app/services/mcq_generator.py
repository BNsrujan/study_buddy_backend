from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
tokenizer = AutoTokenizer.from_pretrained("t5-small")
question_generator = pipeline("question-generation", model=model, tokenizer=tokenizer)

def generate_mcqs(text: str) -> list:
    return question_generator(text)
