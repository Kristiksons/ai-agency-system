from services.openai_client import generate


def create_calendar(client):

    prompt = f"""
Niche: {client["niche"]}

Create a 7-day Instagram content plan.

Make it diverse, strategic, and realistic.
"""

    data = generate(prompt)

    calendar = []

    if not isinstance(data, list):
        return []

    i = 0
    while i < len(data):

        item = data[i]

        score = item.get("score", 75)

        calendar.append({
            "day": item.get("day", f"Day {i+1}"),
            "idea": item.get("hook", ""),
            "caption": item.get("caption", ""),
            "hashtags": item.get("hashtags", ""),
            "reel_script": item.get("reel_script", ""),
            "why": item.get("why", ""),
            "score": score
        })

        i += 1

    return calendar


def generate_strategy_insight(calendar, niche):

    if len(calendar) == 0:
        return "No data available."

    total = 0
    i = 0
    while i < len(calendar):
        total += calendar[i]["score"]
        i += 1

    avg = total / len(calendar)

    best = max(calendar, key=lambda x: x["score"])
    worst = min(calendar, key=lambda x: x["score"])

    insight = f"""
STRATEGY ANALYSIS FOR NICHE: {niche}

Overall Performance:
- Average Score: {round(avg, 1)}
- Best Post: {best['idea']} (Score: {best['score']})
- Weakest Post: {worst['idea']} (Score: {worst['score']})

Strategic Summary:
- This week is { "strong" if avg > 80 else "moderate" if avg > 75 else "weak" } in performance potential.
- Content is strongest in high-engagement hooks and weakest in consistency of depth.

Recommendations:
- Double down on viral hook style used in best post
- Improve weaker posts by adding emotional triggers or storytelling
- Avoid repetitive caption structure across days
"""

    return insight