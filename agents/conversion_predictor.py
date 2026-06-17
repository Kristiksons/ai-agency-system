def predict_conversion(text):

    score = 0

    text = text.lower()

    # strong client signals
    if "business" in text:
        score += 3
    if "clients" in text:
        score += 5
    if "dm" in text:
        score += 5
    if "leads" in text:
        score += 4
    if "sales" in text:
        score += 4
    if "revenue" in text:
        score += 3

    # weak signals
    if "motivation" in text:
        score -= 5
    if "inspire" in text:
        score -= 3

    return score
