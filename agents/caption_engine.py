def generate_caption(idea):

    prompt = f"""
You are an elite Instagram copywriter.

Turn this idea into a full Instagram caption:

Idea:
{idea}

Rules:
- start with a strong hook
- make it short and punchy
- focus on business owners
- include storytelling or pain point
- end with a CTA for DMs
- no fluff

Return only the caption.
"""

    return prompt
