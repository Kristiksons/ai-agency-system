from services.openai_client import generate


def create_calendar(client):

    prompt = f"""
You are an elite social media strategist.

Create 7 Instagram posts for:

Niche: {client["niche"]}

For each post include:
- Hook (must be emotional or attention-grabbing)
- Caption (ready to post)
- Hashtags (5-10 relevant ones)
- Reel Script (short structure)
- Best Time (posting time)

IMPORTANT:
Each post must be completely different in style:
viral, educational, storytelling, controversial, authority, engagement, sales.

Also add a short explanation for EACH post:
"Why this post will perform well"

FORMAT EXACTLY:

Day 1:
Hook: ...
Caption: ...
Hashtags: ...
Reel Script: ...
Best Time: ...
Why it works: ...

(repeat for Day 2 - Day 7)
"""

    result = generate(prompt)

    lines = result.split("\n")

    calendar = []

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    current = {
        "hook": "",
        "caption": "",
        "hashtags": "",
        "reel_script": "",
        "best_time": "",
        "why": ""
    }

    i = 0
    d = 0

    while i < len(lines) and d < 7:

        line = lines[i].strip()

        if line.startswith("Day"):

            if current["hook"] != "" or current["caption"] != "":

                calendar.append({
                    "day": days[d],
                    "idea": current["hook"],
                    "caption": current["caption"],
                    "hashtags": current["hashtags"],
                    "reel_script": current["reel_script"],
                    "best_time": current["best_time"],
                    "why": current["why"],
                    "score": 80 + d
                })

                d += 1

                current = {
                    "hook": "",
                    "caption": "",
                    "hashtags": "",
                    "reel_script": "",
                    "best_time": "",
                    "why": ""
                }

        elif "Hook:" in line:
            current["hook"] = line.replace("Hook:", "").strip()

        elif "Caption:" in line:
            current["caption"] = line.replace("Caption:", "").strip()

        elif "Hashtags:" in line:
            current["hashtags"] = line.replace("Hashtags:", "").strip()

        elif "Reel Script:" in line:
            current["reel_script"] = line.replace("Reel Script:", "").strip()

        elif "Best Time:" in line:
            current["best_time"] = line.replace("Best Time:", "").strip()

        elif "Why it works:" in line:
            current["why"] = line.replace("Why it works:", "").strip()

        i += 1

    # fallback safety
    if len(calendar) == 0:

        fallback = [
            "Strong emotional hook",
            "Educational value",
            "Relatable problem",
            "Controversial angle",
            "Proof/authority",
            "Engagement trigger",
            "Clear offer"
        ]

        i = 0
        while i < 7:

            calendar.append({
                "day": days[i],
                "idea": fallback[i],
                "caption": fallback[i],
                "hashtags": "#marketing #growth #business #socialmedia #tips",
                "reel_script": "Hook → Value → CTA",
                "best_time": "6-9 PM",
                "why": "This post is optimized for engagement",
                "score": 70 + i
            })

            i += 1

    return calendar