def score_content(text):

    score = 0

    text = text.lower()

    # high-value client signals
    if "business" in text:
        score += 3
    if "clients" in text:
        score += 5
    if "dm" in text:
        score += 5
    if "sales" in text:
        score += 4
    if "leads" in text:
        score += 4

    # weak content signals
    if "motivation" in text:
        score -= 5
    if "inspire" in text:
        score -= 3

    return score
