import random

def generate(prompt):

    hook_templates = [
        "The biggest mistake {niche} creators make",
        "Why your {niche} content isn't growing",
        "Nobody tells you this about {niche}",
        "This is what's stopping your {niche} growth",
        "Do this if you're serious about {niche}"
    ]

    caption_templates = [
        "Most people in {niche} overthink content. Simplicity wins.",
        "If you're not consistent in {niche}, you're invisible.",
        "Growth in {niche} comes from repetition, not luck.",
        "Stop chasing trends and focus on value in {niche}.",
        "The fastest way to grow in {niche} is clarity + consistency."
    ]

    why_templates = [
        "High emotional hook increases retention in first 3 seconds",
        "Relatable pain point drives engagement and shares",
        "Educational value improves saves and watch time",
        "Controversial framing boosts comments and interaction",
        "Simple structure improves completion rate"
    ]

    hashtags = "#content #marketing #growth #business #strategy"

    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    # try to extract niche from prompt (simple hack)
    niche = "business"
    if "niche:" in prompt.lower():
        try:
            niche = prompt.lower().split("niche:")[1].split("\n")[0].strip()
        except:
            niche = "business"

    result = ""

    i = 0
    while i < 7:

        hook = random.choice(hook_templates).replace("{niche}", niche)
        caption = random.choice(caption_templates).replace("{niche}", niche)
        why = random.choice(why_templates)

        result += f"""
Day {i+1}:
Hook: {hook}
Caption: {caption}
Hashtags: {hashtags}
Reel Script: Hook → Value → CTA
Best Time: {random.choice(["6-9 AM", "12-2 PM", "6-9 PM"])}
Why it works: {why}
"""

        i += 1

    return result