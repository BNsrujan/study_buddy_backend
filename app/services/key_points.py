def generate_key_points(text: str) -> list:
    # This would be more sophisticated in production; here we split by important sentences
    return text.split(". ")[:5]  # Example, taking the first few sentences
