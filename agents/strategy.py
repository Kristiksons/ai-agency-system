def improve_idea(idea):

    prompt = f"""
You are a senior Instagram marketing strategist.

Improve this content idea so it attracts BUSINESS CLIENTS (not likes).

Idea:
{idea}

Return in this format:

Hook:
Improved Idea:
Why it works:
CTA:
"""

    return prompt