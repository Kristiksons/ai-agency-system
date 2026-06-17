def analyze_history(history):

    if not history:
        return {
            "avg_score": 0,
            "best_day": "none",
            "message": "No data yet"
        }

    total = 0
    best = -1
    best_day = "none"

    i = 0
    while i < len(history):

        run = history[i]

        j = 0
        while j < len(run):

            item = run[j]

            post = item.get("post", item)

            idea = post.get("idea", "").lower()

            score = 0

            if "business" in idea:
                score += 3
            if "clients" in idea:
                score += 5
            if "dm" in idea:
                score += 4
            if "leads" in idea:
                score += 4

            total += score

            if score > best:
                best = score
                best_day = item.get("day", "unknown")

            j += 1

        i += 1

    avg = total / (len(history) if len(history) > 0 else 1)

    return {
        "avg_score": avg,
        "best_day": best_day,
        "message": "Analysis complete"
    }