def score_idea(text):

    score = 0

    text_lower = text.lower()

    # client-focused keywords
    if "business" in text_lower:
        score += 3
    if "clients" in text_lower:
        score += 5
    if "dm" in text_lower:
        score += 5
    if "mistake" in text_lower:
        score += 2
    if "grow" in text_lower:
        score += 2

    # penalize fluff
    if "motivation" in text_lower:
        score -= 5
    if "believe" in text_lower:
        score -= 3

    return score