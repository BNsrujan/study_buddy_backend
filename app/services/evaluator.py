def evaluate_mcq(user_answers: list, correct_answers: list) -> dict:
    score = sum([1 for u, c in zip(user_answers, correct_answers) if u == c])
    return {"score": score, "total": len(correct_answers)}
