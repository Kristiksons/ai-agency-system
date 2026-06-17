def generate_reel_script(idea):

    prompt = f"""
You are an expert Instagram Reels strategist.

Turn this idea into a viral reel script:

Idea:
{idea}

Return this format:

Hook (first 3 seconds):
Scene breakdown (what happens visually):
Voiceover:
On-screen text:
CTA:

Rules:
- must be attention-grabbing
- focus on business owners
- make it simple to film
"""

    return prompt
