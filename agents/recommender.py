def recommend_next_post(calendar):

    if len(calendar) == 0:
        return "Generate a strategy first."

    # find best performing idea
    best = calendar[0]

    i = 0
    while i < len(calendar):
        if calendar[i]["score"] > best["score"]:
            best = calendar[i]
        i += 1

    return {
        "next_post_idea": best["idea"],
        "reason": "This is based on highest predicted viral score from current strategy.",
        "format": "Hook → Value → CTA",
        "suggestion": "Double down on similar content style"
    }