def evaluate(answers: dict, correct_answers: dict) -> dict:
    evaluation = {
        question: (answers[question] == correct_answer)
        for question, correct_answer in correct_answers.items()
    }
    return evaluation
