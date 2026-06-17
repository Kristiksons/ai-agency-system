import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate(prompt):

    system_prompt = """
You are a world-class social media strategist working inside a top marketing agency.

Your job is to create HIGH VARIETY, NON-REPETITIVE weekly content plans.

You must think like a strategist, not a template generator.

Return ONLY valid JSON array with 7 items.

Each item:

{
  "day": "Monday",
  "hook": "...",
  "caption": "...",
  "hashtags": "...",
  "reel_script": "...",
  "best_time": "...",
  "why": "..."
}

🔥 IMPORTANT STRATEGY RULES:
Each day MUST follow a different content angle:

- Monday: attention-grabbing viral hook
- Tuesday: educational value post
- Wednesday: storytelling / real example
- Thursday: controversial opinion
- Friday: authority / credibility building
- Saturday: engagement / question post
- Sunday: soft sales / call to action

🔥 CONTENT RULES:
- Hooks must NOT repeat structure
- Captions must be specific, not generic advice
- Include real-world style phrasing (not AI-sounding)
- No filler sentences like "this is important"
- Each post should feel like a real Instagram creator wrote it

🔥 OUTPUT RULE:
Return ONLY JSON. No markdown. No explanations.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.95
    )

    content = response.choices[0].message.content

    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        return []
    except:
        return []