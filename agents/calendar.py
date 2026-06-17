import json
from services.openai_client import generate


# ---------------- CREATE WEEKLY CALENDAR ----------------
def create_calendar(client):

    prompt = f"""
You are a social media strategist.

Return ONLY valid JSON (no markdown, no explanation).

Create a 7-day Instagram content plan for this niche:
{client["niche"]}

Format exactly like this:

[
  {{
    "day": "Monday",
    "idea": "content idea",
    "caption": "caption text",
    "score": 85
  }}
]

Return 7 items.
"""

    response = generate(prompt)

    try:
        data = json.loads(response)
    except:
        return []

    calendar = []

    i = 0
    while i < len(data):
        item = data[i]

        calendar.append({
            "day": item.get("day", ""),
            "idea": item.get("idea", ""),
            "caption": item.get("caption", ""),
            "score": item.get("score", 75)
        })

        i += 1

    return calendar


# ---------------- STRATEGY INSIGHTS ----------------
def generate_strategy_insight(calendar, niche):

    if not calendar:
        return "No data available."

    total = 0
    i = 0

    while i < len(calendar):
        total += calendar[i]["score"]
        i += 1

    avg = total / len(calendar)

    best = max(calendar, key=lambda x: x["score"])
    worst = min(calendar, key=lambda x: x["score"])

    return f"""
🧠 STRATEGY INSIGHTS

Niche: {niche}

📊 Average Score: {round(avg, 1)}

🔥 Best Idea:
{best['idea']} (Score {best['score']})

⚠️ Weakest Idea:
{worst['idea']} (Score {worst['score']})

💡 Recommendation:
- Improve hooks for lower-performing posts
- Double down on high-score content styles
- Add more emotional storytelling and curiosity gaps
"""


# ---------------- REGENERATE SINGLE DAY ----------------
def regenerate_day(niche, day):

    prompt = f"""
You are a social media expert.

Improve this single content idea.

Niche: {niche}
Day: {day}

Return ONLY valid JSON:

{{
  "idea": "improved idea",
  "caption": "improved caption",
  "score": 90
}}
"""

    response = generate(prompt)

    try:
        data = json.loads(response)
    except:
        return None

    return data