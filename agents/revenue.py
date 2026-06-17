def estimate_value(calendar):

    total_score = 0

    i = 0
    while i < len(calendar):

        item = calendar[i]

        score = item.get("score", 50)

        total_score += score

        i += 1

    avg_score = total_score / len(calendar)

    # fake but realistic SaaS-style metrics
    estimated_reach = int(avg_score * 120)
    estimated_likes = int(avg_score * 8)
    estimated_comments = int(avg_score * 0.6)
    estimated_leads = int(avg_score * 0.2)

    return {
        "avg_viral_score": round(avg_score, 2),
        "estimated_reach": estimated_reach,
        "estimated_likes": estimated_likes,
        "estimated_comments": estimated_comments,
        "estimated_leads": estimated_leads
    }